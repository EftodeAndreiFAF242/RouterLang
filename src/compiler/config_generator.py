"""
RouterLang Config Generator
============================
Translates a .rl source file into per-device router configuration files
(Cisco IOS-style).

This module does NOT rely on symbol_table.py or semantic_checker.py.
It parses the ANTLR tree directly with its own lightweight listener,
so it is immune to grammar-mismatch bugs in those modules.

One .cfg file is produced per concrete device declared in the `devices`
section.  If no devices section exists, synthetic names are derived from
role counts (e.g. R-SPINE-1, R-SPINE-2).

Output files are written to a directory chosen by the caller.

Usage (standalone):
    python src/compiler/config_generator.py my_network.rl
    python src/compiler/config_generator.py my_network.rl --out-dir ./configs

Usage (from main.py via --generate flag):
    python main.py my_network.rl --generate
    python main.py my_network.rl --generate --out-dir ./configs
"""

import os
import sys
import textwrap
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# -- path setup so the module works both stand-alone and when imported
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "parser"))


# ===============================================================================
# Data classes -- what we collect from the parse tree
# ===============================================================================

@dataclass
class RoleInfo:
    name:  str
    count: int = 1
    asn:   Optional[int] = None

@dataclass
class LinkInfo:
    role1:  str
    role2:  str
    weight: int = 1

@dataclass
class PolicyInfo:
    name:  str
    ranks: list = field(default_factory=list)   # list of int

@dataclass
class IntentInfo:
    name:         str
    primary_path: list = field(default_factory=list)
    backup_path:  list = field(default_factory=list)
    policy_ref:   Optional[str] = None
    fault_tol:    int = 0

@dataclass
class NetworkModel:
    """Everything the config generator needs, extracted directly from the tree."""
    roles:       dict = field(default_factory=dict)   # name -> RoleInfo
    links:       list = field(default_factory=list)   # list of LinkInfo
    devices:     dict = field(default_factory=dict)   # device_name -> role_name
    policies:    list = field(default_factory=list)   # list of PolicyInfo
    intents:     list = field(default_factory=list)   # list of IntentInfo
    ospf_areas:  dict = field(default_factory=dict)   # area_id(int) -> [role_name,...]
    rr_role:     Optional[str] = None


# ===============================================================================
# ANTLR listener -- walks the parse tree and fills a NetworkModel
# ===============================================================================

def _parse_network(source: str) -> NetworkModel:
    """
    Parse *source* (RouterLang text) and return a NetworkModel.
    Uses its own listener so it never touches symbol_table.py.
    """
    from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
    from RouterLangLexer    import RouterLangLexer
    from RouterLangParser   import RouterLangParser
    from RouterLangListener import RouterLangListener

    model = NetworkModel()

    class Collector(RouterLangListener):
        # -- topology / roles
        def enterRoleDecl(self, ctx):
            name = ctx.IDENT().getText()
            # Grammar: roleDecl : IDENT '{' 'count' ':' intRange '}'
            # intRange : INT ('..' INT)?
            ints = [int(t.getText()) for t in ctx.intRange().INT()]
            count = max(ints) if ints else 1
            model.roles[name] = RoleInfo(name=name, count=count)

        # -- topology / links
        def enterLinkDecl(self, ctx):
            idents = [t.getText() for t in ctx.IDENT()]
            if len(idents) >= 2:
                weight = 1
                if ctx.INT():
                    weight = int(ctx.INT().getText())
                model.links.append(LinkInfo(role1=idents[0], role2=idents[1], weight=weight))

        # -- topology / devices
        def enterDeviceBinding(self, ctx):
            role_name = ctx.IDENT().getText()
            dev_names = [t.getText() for t in ctx.deviceList().IDENT()]
            for dev in dev_names:
                model.devices[dev] = role_name

        # -- routing / bgp / asn
        def enterRoleAsn(self, ctx):
            role_name = ctx.IDENT().getText()
            asn_val   = int(ctx.INT().getText())
            if role_name in model.roles:
                model.roles[role_name].asn = asn_val

        # -- routing / bgp / route-reflector
        def enterRrDecl(self, ctx):
            model.rr_role = ctx.IDENT().getText()

        # -- routing / ospf / area
        def enterAreaDecl(self, ctx):
            area_id = int(ctx.INT().getText())
            roles   = [t.getText() for t in ctx.roleList().IDENT()]
            model.ospf_areas[area_id] = roles

        # -- policy
        def enterPolicyDef(self, ctx):
            pol_name = ctx.IDENT().getText()
            ranks = []
            for stanza in ctx.policyStanza():
                rc = stanza.rankClause()
                if rc:
                    ranks.append(int(rc.INT().getText()))
            model.policies.append(PolicyInfo(name=pol_name, ranks=ranks))

        # -- intent
        def enterIntentDecl(self, ctx):
            intent_name = ctx.IDENT(0).getText()
            intent = IntentInfo(name=intent_name)

            rb = ctx.routeBody()
            if rb is None:
                model.intents.append(intent)
                return

            ps = rb.pathSpec()
            if ps:
                path_exprs = ps.pathExpr()
                if len(path_exprs) >= 1:
                    intent.primary_path = [t.getText() for t in path_exprs[0].IDENT()]
                if len(path_exprs) >= 2:
                    intent.backup_path  = [t.getText() for t in path_exprs[1].IDENT()]

            pr = rb.policyRef()
            if pr:
                intent.policy_ref = pr.IDENT().getText()

            ft = rb.ftSpec()
            if ft:
                intent.fault_tol = int(ft.INT().getText())

            model.intents.append(intent)

    # actually walk the tree
    input_stream = InputStream(source)
    lexer   = RouterLangLexer(input_stream)
    stream  = CommonTokenStream(lexer)
    parser  = RouterLangParser(stream)
    parser.removeErrorListeners()   # suppress noise; main.py already validated
    tree    = parser.program()

    ParseTreeWalker.DEFAULT.walk(Collector(), tree)
    return model


# ===============================================================================
# DeviceConfig -- one per physical device we will emit a .cfg for
# ===============================================================================

@dataclass
class DeviceConfig:
    hostname:   str
    role:       str
    asn:        Optional[int]
    is_rr:      bool
    bgp_peers:  list    # [(peer_hostname, peer_asn), ...]
    ospf_areas: list    # [area_id, ...]
    policies:   list    # [PolicyInfo, ...]
    intents:    list    # [IntentInfo, ...]


# ===============================================================================
# Config Generator
# ===============================================================================

class ConfigGenerator:

    def __init__(self, model: NetworkModel, source_name: str = ""):
        self.model       = model
        self.source_name = source_name

    # -- public API

    def generate(self) -> dict:
        """Return {hostname: config_text}."""
        configs = {}
        for dc in self._build_device_configs():
            configs[dc.hostname] = self._render(dc)
        return configs

    def write(self, out_dir: str) -> list:
        """Write all .cfg files to out_dir.  Returns sorted list of paths."""
        os.makedirs(out_dir, exist_ok=True)
        written = []
        for hostname, text in self.generate().items():
            safe = hostname.replace("/", "_").replace("\\", "_")
            path = os.path.join(out_dir, f"{safe}.cfg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            written.append(path)
        return sorted(written)

    # -- build per-device configs

    def _build_device_configs(self) -> list:
        m = self.model

        # role -> [device_names]
        role_to_devs = {}
        if m.devices:
            for dev_name, role_name in m.devices.items():
                role_to_devs.setdefault(role_name, []).append(dev_name)
        else:
            # synthesise from role counts
            for role_name, ri in m.roles.items():
                devs = [f"R-{role_name.upper()}-{i}" for i in range(1, ri.count + 1)]
                role_to_devs[role_name] = devs

        # role -> [ospf_area_ids]
        role_to_areas = {}
        for area_id, roles in m.ospf_areas.items():
            for r in roles:
                role_to_areas.setdefault(r, []).append(area_id)

        result = []
        for role_name, dev_names in role_to_devs.items():
            ri    = m.roles.get(role_name, RoleInfo(name=role_name))
            is_rr = (m.rr_role == role_name)

            for dev_name in dev_names:
                dc = DeviceConfig(
                    hostname   = dev_name,
                    role       = role_name,
                    asn        = ri.asn,
                    is_rr      = is_rr,
                    bgp_peers  = self._peers_for(role_name, role_to_devs),
                    ospf_areas = sorted(role_to_areas.get(role_name, [])),
                    policies   = list(m.policies),
                    intents    = list(m.intents),
                )
                result.append(dc)
        return result

    def _peers_for(self, role_name: str, role_to_devs: dict) -> list:
        adjacent = set()
        for lnk in self.model.links:
            if lnk.role1 == role_name:
                adjacent.add(lnk.role2)
            elif lnk.role2 == role_name:
                adjacent.add(lnk.role1)
        peers = []
        for adj_role in sorted(adjacent):
            adj_asn = self.model.roles[adj_role].asn if adj_role in self.model.roles else None
            for peer_dev in role_to_devs.get(adj_role, []):
                peers.append((peer_dev, adj_asn))
        return peers

    # -- rendering

    def _render(self, dc: DeviceConfig) -> str:
        parts = [self._header(dc), self._hostname(dc)]
        if dc.ospf_areas:
            parts.append(self._ospf(dc))
        if dc.asn is not None:
            parts.append(self._bgp(dc))
        if dc.policies:
            parts.append(self._policy(dc))
        if dc.intents:
            parts.append(self._intents(dc))
        parts.append("!\nend\n")
        return "\n".join(parts)

    def _header(self, dc: DeviceConfig) -> str:
        ts  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src = self.source_name or "RouterLang"
        return (
            f"! {'=' * 58}\n"
            f"! Auto-generated by RouterLang\n"
            f"! Source    : {src}\n"
            f"! Device    : {dc.hostname}\n"
            f"! Role      : {dc.role}\n"
            f"! Generated : {ts}\n"
            f"! {'=' * 58}\n"
            f"!\n"
            f"! WARNING: Review carefully before applying to a live device.\n"
            f"!\n"
        )

    def _hostname(self, dc: DeviceConfig) -> str:
        return f"hostname {dc.hostname}\n"

    def _ospf(self, dc: DeviceConfig) -> str:
        rid = _stable_id(dc.hostname)
        lines = ["!", "! -- OSPF " + "-" * 48]
        for area_id in dc.ospf_areas:
            lines += [
                "router ospf 1",
                f"  router-id 0.0.0.{rid}",
                f"  network 0.0.0.0 255.255.255.255 area {area_id}",
                "!",
            ]
        return "\n".join(lines) + "\n"

    def _bgp(self, dc: DeviceConfig) -> str:
        rid = _stable_id(dc.hostname)
        lines = [
            "!", "! -- BGP " + "-" * 49,
            f"router bgp {dc.asn}",
            f"  bgp router-id 0.0.0.{rid}",
        ]
        if dc.is_rr:
            lines += [
                "  bgp cluster-id 1",
                "  ! This device acts as a BGP Route Reflector",
            ]
        for peer_host, peer_asn in dc.bgp_peers:
            peer_ip      = _stable_ip(peer_host)
            peer_asn_str = str(peer_asn) if peer_asn is not None else "UNKNOWN"
            lines += [
                "  !",
                f"  neighbor {peer_ip} remote-as {peer_asn_str}",
                f"  neighbor {peer_ip} description {peer_host}",
                f"  neighbor {peer_ip} update-source Loopback0",
            ]
            if dc.is_rr:
                lines.append(f"  neighbor {peer_ip} route-reflector-client")
        lines.append("!")
        return "\n".join(lines) + "\n"

    def _policy(self, dc: DeviceConfig) -> str:
        lines = ["!", "! -- Route-maps " + "-" * 42]
        for pol in dc.policies:
            seq = 10
            for rank in sorted(pol.ranks):
                lines += [
                    f"route-map {pol.name} permit {seq}",
                    f"  ! rank {rank} -- add match/set clauses here",
                ]
                seq += 10
            lines.append("!")
        return "\n".join(lines) + "\n"

    def _intents(self, dc: DeviceConfig) -> str:
        lines = ["!", "! -- Traffic Intents " + "-" * 37]
        for intent in dc.intents:
            primary = " >> ".join(intent.primary_path) or "-"
            backup  = " >> ".join(intent.backup_path)  or "none"
            lines += [
                f"! Intent          : {intent.name}",
                f"!   Primary path  : {primary}",
                f"!   Backup  path  : {backup}",
            ]
            if intent.policy_ref:
                lines += [
                    f"!   Policy        : {intent.policy_ref}",
                    f"!   -> apply route-map {intent.policy_ref} inbound/outbound on relevant interfaces",
                ]
            if intent.fault_tol:
                lines.append(f"!   Fault-tolerance: k={intent.fault_tol}")
            lines.append("!")
        return "\n".join(lines) + "\n"


# ===============================================================================
# Helpers
# ===============================================================================

def _stable_id(name: str, mod: int = 253) -> int:
    """Deterministic 1..mod integer from a device name (for router-ids / IPs)."""
    h = 0
    for ch in name:
        h = (h * 31 + ord(ch)) & 0xFFFF
    return (h % mod) + 1


def _stable_ip(hostname: str) -> str:
    """Deterministic loopback-style IP (10.0.0.x) for a device."""
    return f"10.0.0.{_stable_id(hostname)}"


# ===============================================================================
# Public entry point used by main.py
# ===============================================================================

def generate_configs(source: str, source_name: str, out_dir: str) -> list:
    """
    Parse *source*, generate one .cfg per device, write to *out_dir*.
    Returns sorted list of written file paths.
    """
    model = _parse_network(source)
    gen   = ConfigGenerator(model, source_name=source_name)
    return gen.write(out_dir)


# ===============================================================================
# Stand-alone entry point
# ===============================================================================

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(
        description="RouterLang Config Generator -- generate .cfg files from a .rl source"
    )
    ap.add_argument("file",      help="Path to a .rl source file")
    ap.add_argument("--out-dir", default="", help="Output directory (default: ./output/<name>/)")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: file not found: {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        source = f.read()

    basename = os.path.splitext(os.path.basename(args.file))[0]
    out_dir  = args.out_dir or os.path.join("output", basename)

    print(f"\nGenerating configs for '{args.file}' -> '{out_dir}/'")
    written = generate_configs(source, args.file, out_dir)
    for p in written:
        print(f"  OK  {p}")
    print(f"\n{len(written)} config file(s) written.")