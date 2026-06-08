"""
RouterLang Config Generator
============================
Translates a .rl source file into per-device router configuration files.

Supported vendors (--vendor flag in main.py):
    cisco      Cisco IOS-style CLI  (default)
    junos      JunOS hierarchical CLI (set-style)
    openconfig OpenConfig JSON (RFC 7951)

IPAM support:
    Pass --ipam <path/to/ipam.csv> to use real IP addresses instead of
    hash-derived ones. The CSV must have columns: device, loopback_ip, mgmt_ip
    Example:
        device,loopback_ip,mgmt_ip
        R-SPINE-1,10.0.1.1,192.168.1.1
        R-LEAF-1,10.0.2.1,192.168.1.11

    If no CSV is provided, or a device is not found in the CSV,
    the generator falls back to the original hash-based IP automatically.

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
    python src/compiler/config_generator.py my_network.rl --vendor junos
    python src/compiler/config_generator.py my_network.rl --vendor openconfig
    python src/compiler/config_generator.py my_network.rl --ipam ipam.csv

Usage (from main.py via --generate flag):
    python main.py my_network.rl --generate
    python main.py my_network.rl --generate --vendor junos
    python main.py my_network.rl --generate --vendor openconfig --out-dir ./configs
    python main.py my_network.rl --generate --ipam ipam.csv
    python main.py my_network.rl --generate --vendor junos --ipam ipam.csv
"""

import os
import sys
import csv
import json
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
class PolicyStanzaInfo:
    rank:    Optional[int]
    action:  str           # "permit" or "deny"
    prefix:  Optional[str] = None
    le:      Optional[int] = None
    match_any: bool        = False
    local_pref: Optional[int] = None

@dataclass
class PolicyInfo:
    name:     str
    ranks:    list = field(default_factory=list)       # list of int
    stanzas:  list = field(default_factory=list)       # list of PolicyStanzaInfo

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
            ranks    = []
            stanzas  = []
            for stanza in ctx.policyStanza():
                rank = None
                rc = stanza.rankClause()
                if rc:
                    rank = int(rc.INT().getText())
                    ranks.append(rank)

                action = "permit"
                ak = stanza.actionKw()
                if ak:
                    action = ak.getText()

                prefix     = None
                le_val     = None
                match_any  = False
                local_pref = None

                for mc in stanza.matchClause():
                    me = mc.matchExpr()
                    if me.getText() == "any":
                        match_any = True
                    elif me.prefixExpr():
                        pe = me.prefixExpr()
                        prefix = pe.CIDR().getText() if pe.CIDR() else None
                        if pe.INT():
                            le_val = int(pe.INT().getText())

                for sc in stanza.setClause():
                    se = sc.setExpr()
                    if se.KW_LOCAL_PREF() and se.INT():
                        local_pref = int(se.INT().getText())

                stanzas.append(PolicyStanzaInfo(
                    rank=rank,
                    action=action,
                    prefix=prefix,
                    le=le_val,
                    match_any=match_any,
                    local_pref=local_pref,
                ))

            model.policies.append(PolicyInfo(name=pol_name, ranks=ranks, stanzas=stanzas))

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
    parser.removeErrorListeners()
    tree    = parser.program()

    ParseTreeWalker.DEFAULT.walk(Collector(), tree)
    return model


# ===============================================================================
# IPAM loader
# ===============================================================================

def load_ipam(csv_path: str) -> dict:
    """
    Load a CSV file mapping device names to IP addresses.

    Expected CSV format:
        device,loopback_ip,mgmt_ip
        R-SPINE-1,10.0.1.1,192.168.1.1
        R-LEAF-1,10.0.2.1,192.168.1.11

    Returns:
        {hostname: {"loopback_ip": "...", "mgmt_ip": "..."}}

    Falls back gracefully if the file does not exist or a row is malformed.
    Devices not present in the CSV will automatically use hash-based IPs.
    """
    ipam = {}
    if not csv_path or not os.path.isfile(csv_path):
        return ipam
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            device = row.get("device", "").strip()
            if device:
                ipam[device] = {
                    "loopback_ip": row.get("loopback_ip", "").strip(),
                    "mgmt_ip":     row.get("mgmt_ip", "").strip(),
                }
    return ipam


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
# Base Config Generator  (vendor-neutral scaffold)
# ===============================================================================

class ConfigGenerator:

    VENDOR = "cisco"   # overridden by subclasses
    EXT    = ".cfg"

    def __init__(self, model: NetworkModel, source_name: str = "", ipam: dict = None):
        self.model       = model
        self.source_name = source_name
        self.ipam        = ipam or {}   # {hostname: {loopback_ip, mgmt_ip}}

    # -- IP resolution (IPAM-aware, falls back to hash)

    def _get_ip(self, hostname: str) -> str:
        """
        Return the loopback IP for a device.
        Uses the IPAM table when available, falls back to hash-based IP.
        """
        entry = self.ipam.get(hostname, {})
        return entry.get("loopback_ip") or _stable_ip(hostname)

    def _get_rid(self, hostname: str) -> str:
        """
        Return the router-id for a device.
        Uses IPAM loopback IP when available, falls back to 0.0.0.<hash>.
        """
        entry = self.ipam.get(hostname, {})
        loopback = entry.get("loopback_ip", "")
        return loopback if loopback else f"0.0.0.{_stable_id(hostname)}"

    # -- public API

    def generate(self) -> dict:
        """Return {hostname: config_text}."""
        configs = {}
        for dc in self._build_device_configs():
            configs[dc.hostname] = self._render(dc)
        return configs

    def write(self, out_dir: str) -> list:
        """Write all config files to out_dir.  Returns sorted list of paths."""
        os.makedirs(out_dir, exist_ok=True)
        written = []
        for hostname, text in self.generate().items():
            safe = hostname.replace("/", "_").replace("\\", "_")
            path = os.path.join(out_dir, f"{safe}{self.EXT}")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            written.append(path)
        return sorted(written)

    # -- build per-device configs (shared across all vendors)

    def _build_device_configs(self) -> list:
        m = self.model

        role_to_devs = {}
        if m.devices:
            for dev_name, role_name in m.devices.items():
                role_to_devs.setdefault(role_name, []).append(dev_name)
        else:
            for role_name, ri in m.roles.items():
                devs = [f"R-{role_name.upper()}-{i}" for i in range(1, ri.count + 1)]
                role_to_devs[role_name] = devs

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

    def _render(self, dc: DeviceConfig) -> str:
        raise NotImplementedError


# ===============================================================================
# Cisco IOS Generator
# ===============================================================================

class CiscoConfigGenerator(ConfigGenerator):

    VENDOR = "cisco"
    EXT    = ".cfg"

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
        ip_source = "IPAM" if dc.hostname in self.ipam else "hash-derived"
        return (
            f"! {'=' * 58}\n"
            f"! Auto-generated by RouterLang  [vendor: cisco]\n"
            f"! Source    : {src}\n"
            f"! Device    : {dc.hostname}\n"
            f"! Role      : {dc.role}\n"
            f"! Loopback  : {self._get_ip(dc.hostname)}  ({ip_source})\n"
            f"! Generated : {ts}\n"
            f"! {'=' * 58}\n"
            f"!\n"
            f"! WARNING: Review carefully before applying to a live device.\n"
            f"!\n"
        )

    def _hostname(self, dc: DeviceConfig) -> str:
        return f"hostname {dc.hostname}\n"

    def _ospf(self, dc: DeviceConfig) -> str:
        rid = self._get_rid(dc.hostname)
        lines = ["!", "! -- OSPF " + "-" * 48]
        for area_id in dc.ospf_areas:
            lines += [
                "router ospf 1",
                f"  router-id {rid}",
                f"  network 0.0.0.0 255.255.255.255 area {area_id}",
                "!",
            ]
        return "\n".join(lines) + "\n"

    def _bgp(self, dc: DeviceConfig) -> str:
        rid = self._get_rid(dc.hostname)
        lines = [
            "!", "! -- BGP " + "-" * 49,
            f"router bgp {dc.asn}",
            f"  bgp router-id {rid}",
        ]
        if dc.is_rr:
            lines += [
                "  bgp cluster-id 1",
                "  ! This device acts as a BGP Route Reflector",
            ]
        for peer_host, peer_asn in dc.bgp_peers:
            peer_ip      = self._get_ip(peer_host)
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
            for stanza in pol.stanzas:
                action = "permit" if stanza.action == "permit" else "deny"
                lines.append(f"route-map {pol.name} {action} {seq}")
                if stanza.prefix:
                    le_str = f" le {stanza.le}" if stanza.le else ""
                    lines.append(f"  match ip address prefix-list PL-{pol.name}-{seq}")
                    lines.append(f"ip prefix-list PL-{pol.name}-{seq} seq 5 {action} {stanza.prefix}{le_str}")
                elif stanza.match_any:
                    lines.append(f"  ! match any")
                if stanza.local_pref is not None:
                    lines.append(f"  set local-preference {stanza.local_pref}")
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
# JunOS Generator
# ===============================================================================

class JunOSConfigGenerator(ConfigGenerator):

    VENDOR = "junos"
    EXT    = ".conf"

    def _render(self, dc: DeviceConfig) -> str:
        parts = [self._header(dc)]
        parts.append(self._system(dc))
        if dc.ospf_areas:
            parts.append(self._ospf(dc))
        if dc.asn is not None:
            parts.append(self._bgp(dc))
        if dc.policies:
            parts.append(self._policy(dc))
        if dc.intents:
            parts.append(self._intents(dc))
        return "\n".join(parts)

    def _header(self, dc: DeviceConfig) -> str:
        ts  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src = self.source_name or "RouterLang"
        ip_source = "IPAM" if dc.hostname in self.ipam else "hash-derived"
        return (
            f"/* {'=' * 56} */\n"
            f"/* Auto-generated by RouterLang  [vendor: junos]      */\n"
            f"/* Source    : {src:<44} */\n"
            f"/* Device    : {dc.hostname:<44} */\n"
            f"/* Role      : {dc.role:<44} */\n"
            f"/* Loopback  : {self._get_ip(dc.hostname):<44} */\n"
            f"/* IP source : {ip_source:<44} */\n"
            f"/* Generated : {ts:<44} */\n"
            f"/* WARNING: Review carefully before applying.          */\n"
            f"/* {'=' * 56} */\n"
        )

    def _system(self, dc: DeviceConfig) -> str:
        return (
            f"system {{\n"
            f"    host-name {dc.hostname};\n"
            f"    /* RouterLang role: {dc.role} */\n"
            f"}}\n"
        )

    def _ospf(self, dc: DeviceConfig) -> str:
        rid = self._get_rid(dc.hostname)
        lines = ["protocols {", "    ospf {", f"        router-id {rid};"]
        for area_id in dc.ospf_areas:
            lines += [
                f"        area {area_id} {{",
                f"            interface all;",
                f"        }}",
            ]
        lines += ["    }", "}"]
        return "\n".join(lines) + "\n"

    def _bgp(self, dc: DeviceConfig) -> str:
        rid = self._get_rid(dc.hostname)
        lines = [
            "protocols {",
            "    bgp {",
            f"        local-as {dc.asn};",
        ]
        if dc.is_rr:
            lines.append("        /* This device acts as a BGP Route Reflector */")
        for peer_host, peer_asn in dc.bgp_peers:
            peer_ip      = self._get_ip(peer_host)
            peer_asn_str = str(peer_asn) if peer_asn is not None else "UNKNOWN"
            lines += [
                f"        group {peer_host} {{",
                f"            type external;" if str(peer_asn) != str(dc.asn) else "            type internal;",
                f"            peer-as {peer_asn_str};",
                f"            neighbor {peer_ip} {{",
                f"                description \"{peer_host}\";",
            ]
            if dc.is_rr:
                lines.append(f"                cluster {rid};")
            lines += [
                f"            }}",
                f"        }}",
            ]
        lines += ["    }", "}"]
        return "\n".join(lines) + "\n"

    def _policy(self, dc: DeviceConfig) -> str:
        lines = ["policy-options {"]
        for pol in dc.policies:
            for stanza in pol.stanzas:
                if stanza.prefix:
                    le_str = f" upto /{stanza.le}" if stanza.le else ""
                    lines += [
                        f"    prefix-list PL-{pol.name}-{stanza.rank or 'X'} {{",
                        f"        {stanza.prefix}{le_str};",
                        f"    }}",
                    ]
            lines += [f"    policy-statement {pol.name} {{"]
            for stanza in pol.stanzas:
                term_name = f"term-{stanza.rank}" if stanza.rank is not None else "term-default"
                lines.append(f"        term {term_name} {{")
                lines.append(f"            from {{")
                if stanza.prefix:
                    lines.append(f"                prefix-list PL-{pol.name}-{stanza.rank or 'X'};")
                elif stanza.match_any:
                    lines.append(f"                /* match any */")
                lines.append(f"            }}")
                lines.append(f"            then {{")
                if stanza.action == "permit":
                    lines.append(f"                accept;")
                else:
                    lines.append(f"                reject;")
                if stanza.local_pref is not None:
                    lines.append(f"                local-preference {stanza.local_pref};")
                lines.append(f"            }}")
                lines.append(f"        }}")
            lines += ["    }", "}"]
        return "\n".join(lines) + "\n"

    def _intents(self, dc: DeviceConfig) -> str:
        lines = ["/* -- Traffic Intents " + "-" * 36 + " */"]
        for intent in dc.intents:
            primary = " >> ".join(intent.primary_path) or "-"
            backup  = " >> ".join(intent.backup_path)  or "none"
            lines += [
                f"/* Intent         : {intent.name}",
                f"   Primary path   : {primary}",
                f"   Backup  path   : {backup}",
            ]
            if intent.policy_ref:
                lines.append(f"   Policy         : {intent.policy_ref}  -> apply as import/export policy")
            if intent.fault_tol:
                lines.append(f"   Fault-tolerance: k={intent.fault_tol}")
            lines.append("*/")
        return "\n".join(lines) + "\n"


# ===============================================================================
# OpenConfig JSON Generator
# ===============================================================================

class OpenConfigGenerator(ConfigGenerator):

    VENDOR = "openconfig"
    EXT    = ".json"

    def _render(self, dc: DeviceConfig) -> str:
        ts  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src = self.source_name or "RouterLang"
        rid = self._get_rid(dc.hostname)
        ip_source = "IPAM" if dc.hostname in self.ipam else "hash-derived"

        doc = {
            "_routerlang_meta": {
                "vendor":    "openconfig",
                "source":    src,
                "device":    dc.hostname,
                "role":      dc.role,
                "loopback":  self._get_ip(dc.hostname),
                "ip_source": ip_source,
                "generated": ts,
                "warning":   "Review carefully before applying to a live device.",
            },
            "openconfig-system:system": {
                "config": {"hostname": dc.hostname}
            },
        }

        # BGP
        if dc.asn is not None:
            neighbors = []
            for peer_host, peer_asn in dc.bgp_peers:
                peer_ip = self._get_ip(peer_host)
                neighbor = {
                    "neighbor-address": peer_ip,
                    "config": {
                        "neighbor-address": peer_ip,
                        "peer-as": peer_asn if peer_asn is not None else 0,
                        "description": peer_host,
                    },
                    "transport": {
                        "config": {"local-address": "Loopback0"}
                    },
                }
                if dc.is_rr:
                    neighbor["route-reflector"] = {
                        "config": {
                            "route-reflector-client": True,
                            "route-reflector-cluster-id": rid,
                        }
                    }
                neighbors.append(neighbor)

            doc["openconfig-bgp:bgp"] = {
                "global": {
                    "config": {"as": dc.asn, "router-id": rid}
                },
                "neighbors": {"neighbor": neighbors},
            }

        # OSPF
        if dc.ospf_areas:
            areas = []
            for area_id in dc.ospf_areas:
                areas.append({
                    "identifier": area_id,
                    "config": {"identifier": area_id},
                    "interfaces": {
                        "interface": [
                            {"id": "all", "config": {"id": "all", "passive": False}}
                        ]
                    },
                })
            doc["openconfig-ospfv2:ospfv2"] = {
                "global": {"config": {"router-id": rid}},
                "areas": {"area": areas},
            }

        # Routing policy
        if dc.policies:
            policy_defs = []
            for pol in dc.policies:
                stmts = []
                for stanza in pol.stanzas:
                    term_name = f"term-{stanza.rank}" if stanza.rank is not None else "term-default"
                    conditions = {}
                    if stanza.prefix:
                        conditions["match-prefix-set"] = {
                            "config": {
                                "prefix-set": f"PL-{pol.name}-{stanza.rank or 'X'}",
                                "match-set-options": "ANY",
                            }
                        }
                    actions = {
                        "config": {
                            "policy-result": "ACCEPT_ROUTE" if stanza.action == "permit" else "REJECT_ROUTE",
                        }
                    }
                    if stanza.local_pref is not None:
                        actions["bgp-actions"] = {
                            "config": {"set-local-pref": stanza.local_pref}
                        }
                    stmts.append({
                        "name": term_name,
                        "config": {"name": term_name},
                        "conditions": conditions,
                        "actions": actions,
                    })
                policy_defs.append({
                    "name": pol.name,
                    "config": {"name": pol.name},
                    "statements": {"statement": stmts},
                })
            doc["openconfig-routing-policy:routing-policy"] = {
                "policy-definitions": {"policy-definition": policy_defs}
            }

        # Intents as metadata
        if dc.intents:
            doc["_routerlang_intents"] = [
                {
                    "name":          intent.name,
                    "primary_path":  " >> ".join(intent.primary_path),
                    "backup_path":   " >> ".join(intent.backup_path) or "none",
                    "policy":        intent.policy_ref or "",
                    "fault_tolerance": intent.fault_tol,
                }
                for intent in dc.intents
            ]

        return json.dumps(doc, indent=2) + "\n"


# ===============================================================================
# Factory -- pick the right generator by vendor name
# ===============================================================================

_GENERATORS = {
    "cisco":      CiscoConfigGenerator,
    "junos":      JunOSConfigGenerator,
    "openconfig": OpenConfigGenerator,
}

SUPPORTED_VENDORS = list(_GENERATORS.keys())


def get_generator(vendor: str, model: NetworkModel,
                  source_name: str = "", ipam: dict = None) -> ConfigGenerator:
    """Return the correct ConfigGenerator subclass for *vendor*."""
    vendor = vendor.lower().strip()
    cls = _GENERATORS.get(vendor)
    if cls is None:
        raise ValueError(
            f"Unknown vendor '{vendor}'. "
            f"Supported: {', '.join(SUPPORTED_VENDORS)}"
        )
    return cls(model, source_name=source_name, ipam=ipam or {})


# ===============================================================================
# Public entry point used by main.py
# ===============================================================================

def generate_configs(source: str, source_name: str, out_dir: str,
                     vendor: str = "cisco", ipam_path: str = "") -> list:
    """
    Parse *source*, generate one config file per device, write to *out_dir*.
    Returns sorted list of written file paths.
    """
    model = _parse_network(source)
    ipam  = load_ipam(ipam_path)
    gen   = get_generator(vendor, model, source_name=source_name, ipam=ipam)
    return gen.write(out_dir)


# ===============================================================================
# Stand-alone entry point
# ===============================================================================

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(
        description="RouterLang Config Generator -- generate config files from a .rl source"
    )
    ap.add_argument("file",      help="Path to a .rl source file")
    ap.add_argument("--out-dir", default="", help="Output directory (default: ./output/<name>/)")
    ap.add_argument(
        "--vendor",
        default="cisco",
        choices=SUPPORTED_VENDORS,
        help=f"Target vendor syntax (default: cisco). Choices: {', '.join(SUPPORTED_VENDORS)}",
    )
    ap.add_argument(
        "--ipam",
        default="",
        help="Path to a CSV file mapping device names to IP addresses (optional)",
    )
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: file not found: {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        source = f.read()

    basename = os.path.splitext(os.path.basename(args.file))[0]
    out_dir  = args.out_dir or os.path.join("output", basename)

    print(f"\nGenerating configs for '{args.file}' -> '{out_dir}/'  [vendor: {args.vendor}]")
    if args.ipam:
        print(f"Using IPAM file: {args.ipam}")
    written = generate_configs(source, args.file, out_dir,
                               vendor=args.vendor, ipam_path=args.ipam)
    for p in written:
        print(f"  OK  {p}")
    print(f"\n{len(written)} config file(s) written.")