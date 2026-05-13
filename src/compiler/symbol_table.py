"""
RouterLang Symbol Table
=======================
Walks the ANTLR parse tree and collects every declared symbol
(roles, links, policies, intents, devices) into a structured table.

The symbol table is used by the semantic checker (E-1 through E-14)
and can be printed / dumped to JSON for inspection.

Usage (standalone demo):
    python src/compiler/symbol_table.py

Place this file at:  src/compiler/symbol_table.py
"""

import sys
import os
import json
from dataclasses import dataclass, field, asdict
from typing import Optional

# ── path setup ────────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "parser"))

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from RouterLangLexer   import RouterLangLexer
from RouterLangParser  import RouterLangParser
from RouterLangListener import RouterLangListener

# ── data classes for each symbol kind ────────────────────────────────────────

@dataclass
class RoleSymbol:
    kind:       str = "role"
    name:       str = ""
    count_min:  int = 0
    count_max:  int = 0
    line:       int = 0
    asn:        Optional[int] = None
    linked_to:  list = field(default_factory=list)

@dataclass
class LinkSymbol:
    kind:   str = "link"
    role1:  str = ""
    role2:  str = ""
    weight: int = 1
    line:   int = 0

@dataclass
class DeviceSymbol:
    kind: str = "device"
    name: str = ""
    role: str = ""
    line: int = 0

@dataclass
class PolicySymbol:
    kind:  str = "policy"
    name:  str = ""
    ranks: list = field(default_factory=list)
    line:  int  = 0

@dataclass
class IntentSymbol:
    kind:         str = "intent"
    name:         str = ""
    intent_type:  str = ""
    primary_path: list = field(default_factory=list)
    backup_path:  list = field(default_factory=list)
    policy_ref:   Optional[str] = None
    fault_tol:    int = 0
    scope:        str = "all"
    line:         int = 0

@dataclass
class TransitionSymbol:
    kind:         str = "transition"
    from_topo:    str = ""
    to_topo:      str = ""
    intermediate: Optional[str] = None
    line:         int = 0


# ── Symbol Table ──────────────────────────────────────────────────────────────

class SymbolTable:
    """
    Central registry of all named entities in a RouterLang program.

    Sections
    --------
    roles      : dict[name -> RoleSymbol]
    links      : list[LinkSymbol]
    devices    : dict[name -> DeviceSymbol]
    policies   : dict[name -> PolicySymbol]
    intents    : dict[name -> IntentSymbol]
    transition : TransitionSymbol | None
    """

    def __init__(self):
        self.roles:      dict = {}
        self.links:      list = []
        self.devices:    dict = {}
        self.policies:   dict = {}
        self.intents:    dict = {}
        self.transition: Optional[TransitionSymbol] = None
        self._errors:    list = []

    # ── insertion helpers ──────────────────────────────────────────────────

    def add_role(self, name: str, count_min: int, count_max: int, line: int):
        if name in self.roles:
            self._errors.append(f"E-1: Duplicate role name '{name}' at line {line}")
            return
        if count_min == 0 and count_max == 0:
            self._errors.append(f"E-2: Role '{name}' has count 0 at line {line}")
            return
        if count_min > count_max:
            self._errors.append(
                f"E-3: Role '{name}' range {count_min}..{count_max} is invalid — lower > upper at line {line}"
            )
            return
        self.roles[name] = RoleSymbol(
            name=name, count_min=count_min, count_max=count_max, line=line
        )

    def add_link(self, role1: str, role2: str, weight: int, line: int):
        if role1 == role2:
            self._errors.append(f"E-6: Reflexive link '{role1} -- {role2}' is not allowed (line {line})")
            return
        for r in (role1, role2):
            if r not in self.roles:
                self._errors.append(f"E-4: Link references undeclared role '{r}' at line {line}")
        for existing in self.links:
            if {existing.role1, existing.role2} == {role1, role2}:
                self._errors.append(f"W-5: Duplicate link '{role1} -- {role2}' at line {line}")
        lnk = LinkSymbol(role1=role1, role2=role2, weight=weight, line=line)
        self.links.append(lnk)
        for rname, other in ((role1, role2), (role2, role1)):
            if rname in self.roles and other not in self.roles[rname].linked_to:
                self.roles[rname].linked_to.append(other)

    def add_device(self, name: str, role: str, line: int):
        if name in self.devices:
            self._errors.append(f"Duplicate device name '{name}' at line {line}")
            return
        if role not in self.roles:
            self._errors.append(f"Device '{name}' bound to undeclared role '{role}' at line {line}")
        self.devices[name] = DeviceSymbol(name=name, role=role, line=line)

    def add_policy(self, name: str, ranks: list, line: int):
        if name in self.policies:
            self._errors.append(f"Duplicate policy name '{name}' at line {line}")
            return
        seen = set()
        for r in ranks:
            if r in seen:
                self._errors.append(f"E-7: Duplicate rank {r} in policy '{name}' at line {line}")
            seen.add(r)
        self.policies[name] = PolicySymbol(name=name, ranks=ranks, line=line)

    def add_intent(self, name: str, intent_type: str, primary: list, backup: list,
                   policy_ref: str, fault_tol: int, scope: str, line: int):
        if name in self.intents:
            self._errors.append(f"Duplicate intent name '{name}' at line {line}")
            return
        for path, label in ((primary, "primary"), (backup, "backup")):
            for role in path:
                if role not in self.roles:
                    self._errors.append(
                        f"E-10: {label} path in intent '{name}' references undeclared role '{role}' at line {line}"
                    )
        for path, label in ((primary, "primary"), (backup, "backup")):
            for i in range(len(path) - 1):
                a, b = path[i], path[i + 1]
                if not self._roles_linked(a, b):
                    self._errors.append(
                        f"E-11: No link between consecutive path roles '{a}' and '{b}' "
                        f"in intent '{name}' ({label}) at line {line}"
                    )
        if fault_tol == 0 and intent_type == "route":
            self._errors.append(f"E-13: fault-tolerance k=0 in intent '{name}' at line {line}")
        self.intents[name] = IntentSymbol(
            name=name, intent_type=intent_type,
            primary_path=primary, backup_path=backup,
            policy_ref=policy_ref, fault_tol=fault_tol, scope=scope, line=line
        )

    def set_transition(self, from_topo: str, to_topo: str,
                       intermediate: Optional[str], line: int):
        self.transition = TransitionSymbol(
            from_topo=from_topo, to_topo=to_topo,
            intermediate=intermediate, line=line
        )

    def set_role_asn(self, role: str, asn: int):
        if role in self.roles:
            self.roles[role].asn = asn

    # ── query helpers ──────────────────────────────────────────────────────

    def lookup(self, name: str):
        return (self.roles.get(name)
                or self.policies.get(name)
                or self.intents.get(name)
                or self.devices.get(name))

    def _roles_linked(self, a: str, b: str) -> bool:
        return any(
            {lnk.role1, lnk.role2} == {a, b} for lnk in self.links
        )

    def errors(self) -> list:
        return list(self._errors)

    # ── display ───────────────────────────────────────────────────────────

    def dump(self, as_json: bool = False):
        """Print the full symbol table to stdout."""
        if as_json:
            data = {
                "roles":      {k: asdict(v) for k, v in self.roles.items()},
                "links":      [asdict(l) for l in self.links],
                "devices":    {k: asdict(v) for k, v in self.devices.items()},
                "policies":   {k: asdict(v) for k, v in self.policies.items()},
                "intents":    {k: asdict(v) for k, v in self.intents.items()},
                "transition": asdict(self.transition) if self.transition else None,
            }
            print(json.dumps(data, indent=2))
            return

        SEP   = "─" * 60
        BOLD  = "\033[1m"
        CYAN  = "\033[96m"
        GREEN = "\033[92m"
        RESET = "\033[0m"

        def section(title, items):
            print(f"\n{BOLD}{CYAN}┌─ {title} {'─'*(54-len(title))}┐{RESET}")
            if not items:
                print(f"  {GREEN}(none){RESET}")
            for line in items:
                print(f"  {line}")
            print(f"{BOLD}{CYAN}└{SEP}┘{RESET}")

        # Roles
        role_lines = []
        for name, r in self.roles.items():
            cnt = (f"{r.count_min}" if r.count_min == r.count_max
                   else f"{r.count_min}..{r.count_max}")
            asn_str = f"  ASN={r.asn}" if r.asn else ""
            linked  = ", ".join(r.linked_to) if r.linked_to else "—"
            role_lines.append(
                f"{GREEN}{name:<20}{RESET}  count={cnt:<8}{asn_str:<12}  links=[{linked}]  line={r.line}"
            )
        section("ROLES", role_lines)

        # Links
        link_lines = [
            f"{GREEN}{l.role1:<15}{RESET} -- {GREEN}{l.role2:<15}{RESET}  weight={l.weight}  line={l.line}"
            for l in self.links
        ]
        section("LINKS", link_lines)

        # Devices
        dev_lines = [
            f"{GREEN}{name:<20}{RESET}  role={d.role}  line={d.line}"
            for name, d in self.devices.items()
        ]
        section("DEVICES", dev_lines)

        # Policies
        pol_lines = []
        for name, p in self.policies.items():
            ranks_str = ", ".join(str(r) for r in p.ranks)
            pol_lines.append(
                f"{GREEN}{name:<24}{RESET}  ranks=[{ranks_str}]  line={p.line}"
            )
        section("POLICIES", pol_lines)

        # Intents
        intent_lines = []
        for name, i in self.intents.items():
            primary = " >> ".join(i.primary_path)
            backup  = " >> ".join(i.backup_path) if i.backup_path else "—"
            intent_lines.append(
                f"{GREEN}{name:<20}{RESET}  type={i.intent_type}"
            )
            intent_lines.append(f"   primary : {primary}")
            if i.backup_path:
                intent_lines.append(f"   backup  : {backup}")
            intent_lines.append(
                f"   policy  : {i.policy_ref or '—'}   "
                f"fault-tol={i.fault_tol}   scope={i.scope}   line={i.line}"
            )
        section("INTENTS", intent_lines)

        # Transition
        if self.transition:
            t = self.transition
            section("TRANSITION", [
                f"from={t.from_topo}  to={t.to_topo}  "
                f"intermediate={t.intermediate or '—'}  line={t.line}"
            ])
        else:
            section("TRANSITION", [])

        if self._errors:
            print(f"\n\033[91m{'─'*60}\n  ERRORS / WARNINGS detected during table build:\033[0m")
            for e in self._errors:
                print(f"\033[91m  ✗  {e}\033[0m")
        else:
            print(f"\n\033[92m  ✔  Symbol table built with no errors.\033[0m")


# ── ANTLR listener that populates the symbol table ────────────────────────────

class SymbolTableBuilder(RouterLangListener):
    """
    Listener that walks the parse tree produced by ANTLR and fills
    a SymbolTable instance.

    Attach with ParseTreeWalker.DEFAULT.walk(builder, tree).
    """

    def __init__(self):
        self.table           = SymbolTable()
        self._current_ranks  = []

    # ── topology / roles ──────────────────────────────────────────────────

    def enterRoleDecl(self, ctx):
        name = ctx.IDENT().getText()
        line = ctx.start.line
        # Grammar: roleDecl : IDENT '{' 'count' ':' intRange '}'
        # intRange : INT ('..' INT)?
        ints = [int(t.getText()) for t in ctx.intRange().INT()]
        if len(ints) == 1:
            self.table.add_role(name, ints[0], ints[0], line)
        elif len(ints) >= 2:
            self.table.add_role(name, ints[0], ints[1], line)

    # ── topology / links ──────────────────────────────────────────────────

    def enterLinkDecl(self, ctx):
        # Grammar: linkDecl : IDENT '--' IDENT ('{' 'weight' ':' INT '}')?
        idents = [t.getText() for t in ctx.IDENT()]
        if len(idents) < 2:
            return
        role1, role2 = idents[0], idents[1]
        line = ctx.start.line
        # INT() may return a list; the weight INT is the only one in linkDecl
        weight = 1
        ints = ctx.INT()
        if ints:
            # ctx.INT() returns a list when there are multiple; take the first
            first = ints if not isinstance(ints, list) else ints[0]
            try:
                weight = int(first.getText())
            except Exception:
                weight = 1
        self.table.add_link(role1, role2, weight, line)

    # ── topology / devices ────────────────────────────────────────────────

    def enterDeviceBinding(self, ctx):
        # Grammar: deviceBinding : IDENT ':' '[' deviceList ']'
        # deviceList : IDENT (',' IDENT)* | IDENT '..' IDENT
        role_name = ctx.IDENT().getText()
        line      = ctx.start.line
        dev_names = [t.getText() for t in ctx.deviceList().IDENT()]
        for dev in dev_names:
            self.table.add_device(dev, role_name, line)

    # ── routing / bgp / asn ───────────────────────────────────────────────

    def enterRoleAsn(self, ctx):
        # Grammar: roleAsn : IDENT ':' INT
        role = ctx.IDENT().getText()
        asn  = int(ctx.INT().getText())
        self.table.set_role_asn(role, asn)

    # ── policy ────────────────────────────────────────────────────────────

    def enterPolicyDef(self, ctx):
        self._current_ranks = []

    def enterPolicyStanza(self, ctx):
        # Grammar: policyStanza : rankClause? actionKw '{' ... '}'
        # rankClause : 'rank' INT ':'
        rc = ctx.rankClause()
        if rc:
            self._current_ranks.append(int(rc.INT().getText()))

    def exitPolicyDef(self, ctx):
        name = ctx.IDENT().getText()
        line = ctx.start.line
        self.table.add_policy(name, list(self._current_ranks), line)
        self._current_ranks = []

    # ── intent ────────────────────────────────────────────────────────────

    def enterIntentDecl(self, ctx):
        # Grammar: intentDecl : IDENT ':' 'route' IDENT '{' routeBody '}'
        #                     | IDENT ':' 'constraint' '{' constraintBody '}'
        name = ctx.IDENT(0).getText()
        line = ctx.start.line

        # Determine intent type from the token text
        ctx_text    = ctx.getText()
        intent_type = "route" if ":route" in ctx_text else "constraint"

        primary    = []
        backup     = []
        policy_ref = None
        fault_tol  = 1
        scope      = "all"

        rb = ctx.routeBody()
        if rb:
            ps = rb.pathSpec()
            if ps:
                # Grammar: pathSpec : 'primary' ':' pathExpr ('backup' ':' pathExpr)?
                path_exprs = ps.pathExpr()
                if len(path_exprs) >= 1:
                    primary = [t.getText() for t in path_exprs[0].IDENT()]
                if len(path_exprs) >= 2:
                    backup  = [t.getText() for t in path_exprs[1].IDENT()]

            pr = rb.policyRef()
            if pr:
                policy_ref = pr.IDENT().getText()

            ft = rb.ftSpec()
            if ft:
                fault_tol = int(ft.INT().getText())

            sc = rb.scopeSpec()
            if sc:
                scope = sc.scopeVal().getText()

        self.table.add_intent(
            name, intent_type, primary, backup,
            policy_ref, fault_tol, scope, line
        )

    # ── transition ────────────────────────────────────────────────────────

    def enterTransitionBlock(self, ctx):
        # Grammar: transitionBlock : 'transition' '{' 'from' ':' IDENT 'to' ':' IDENT 'intermediate' ':' IDENT '}'
        idents = [t.getText() for t in ctx.IDENT()]
        line   = ctx.start.line
        from_t = idents[0] if len(idents) > 0 else ""
        to_t   = idents[1] if len(idents) > 1 else ""
        interm = idents[2] if len(idents) > 2 else None
        self.table.set_transition(from_t, to_t, interm, line)


# ── public helper ─────────────────────────────────────────────────────────────

def build_symbol_table(source: str) -> SymbolTable:
    """
    Parse a RouterLang source string and return a populated SymbolTable.
    """
    input_stream = InputStream(source)
    lexer        = RouterLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser       = RouterLangParser(token_stream)
    tree         = parser.program()

    builder = SymbolTableBuilder()
    ParseTreeWalker.DEFAULT.walk(builder, tree)
    return builder.table


# ── standalone demo ───────────────────────────────────────────────────────────

DEMO_SOURCE = """\
topology {
  roles {
    spine  { count: 2 }
    leaf   { count: 1..8 }
    border { count: 2 }
  }
  links {
    spine  -- leaf   { weight: 1 }
    spine  -- border { weight: 2 }
  }
  devices {
    spine:  [R-SPINE-1, R-SPINE-2]
    leaf:   [R-LEAF-1, R-LEAF-2, R-LEAF-3, R-LEAF-4]
    border: [R-BORDER-1, R-BORDER-2]
  }
}
routing {
  bgp {
    asn { spine: 65001  leaf: 65002  border: 65003 }
    neighbors: auto
  }
}
policy {
  define MAIN-POLICY {
    rank 10: permit {
      match prefix 10.0.0.0/8 le 24
      set local-pref 200
      if neighbor.state == LIVE
    }
    rank 20: deny {
      match any
    }
  }
}
intent {
  CORE-TRAFFIC: route backbone {
    primary: border >> spine >> leaf
    backup:  border >> leaf
    apply-policy: MAIN-POLICY
    fault-tolerance: 1
    scope: all
  }
}
"""


if __name__ == "__main__":
    use_json = "--json" in sys.argv

    print("\033[1mRouterLang Symbol Table Builder  —  standalone demo\033[0m")
    print("Parsing built-in demo source ...\n")

    table = build_symbol_table(DEMO_SOURCE)
    table.dump(as_json=use_json)

    print(f"\n\033[90mTip: pass --json for machine-readable output\033[0m\n")