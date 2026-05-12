"""
RouterLang Semantic Checker
============================
Performs semantic analysis over the ANTLR parse tree.

Error catalogue
---------------
E-1   Duplicate role name
E-2   Role count = 0  (meaningless declaration)
E-3   Role range lower > upper
E-4   Link / path / policy-ref references an undeclared role or policy
E-5   Duplicate link edge            (warning — merged, not fatal)
E-6   Reflexive link (role -- role)
E-7   Duplicate rank within the same policy stanza
E-8   Intent references an undeclared policy
E-9   Duplicate intent name
E-10  Path references an undeclared role
E-11  Consecutive path roles are not connected by any link in the topology
E-12  Backup path is identical to the primary path
E-13  fault-tolerance k = 0 on a route intent
E-14  ASN assigned to an undeclared role

Usage (standalone)
------------------
    python src/compiler/semantic_checker.py            # runs built-in test suite
    python src/compiler/semantic_checker.py --verbose  # extra detail
"""

import sys
import os
from dataclasses import dataclass, field
from typing import Optional

# ── path setup so the module works both stand-alone and when imported ──────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "parser"))

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from RouterLangLexer    import RouterLangLexer
from RouterLangParser   import RouterLangParser
from RouterLangListener import RouterLangListener


# ═══════════════════════════════════════════════════════════════════════════════
# Diagnostic types
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SemanticDiagnostic:
    """A single semantic error or warning."""
    code:     str            # "E-1", "W-5", …
    message:  str
    line:     int  = 0
    is_error: bool = True    # False → warning

    def __str__(self):
        kind = "ERROR" if self.is_error else "WARNING"
        loc  = f"  (line {self.line})" if self.line else ""
        return f"[{self.code}] {kind}{loc}: {self.message}"


class SemanticError(Exception):
    """Raised when analysis encounters a fatal error (used in unit-test mode)."""
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Core checker — works with plain Python data (no ANTLR needed here)
# ═══════════════════════════════════════════════════════════════════════════════

class SemanticChecker:
    """
    Accepts facts about a RouterLang program and records errors / warnings.

    Call the  check_*  methods in declaration order:
        1. check_role_decl       for each role
        2. check_link_decl       for each link
        3. check_asn_decl        for each BGP ASN assignment   (optional)
        4. check_policy_rank     for each stanza inside a policy define
        5. check_policy_ref      after all policies are complete
        6. check_path_expr       for each primary / backup path in an intent
        7. check_intent_decl     for each intent (wraps the above)

    After all calls, inspect  .diagnostics  for errors and warnings.
    .has_errors() returns True if any fatal error was recorded.
    """

    def __init__(self):
        self.roles:      dict = {}   # name -> (low, high)
        self.links:      list = []   # (r1, r2) canonical pairs
        self.policies:   dict = {}   # name -> [ranks]
        self.intents:    set  = set()
        self.diagnostics: list = []

    # ── internal helpers ───────────────────────────────────────────────────

    def _err(self, code, msg, line=0):
        self.diagnostics.append(
            SemanticDiagnostic(code=code, message=msg, line=line, is_error=True)
        )

    def _warn(self, code, msg, line=0):
        self.diagnostics.append(
            SemanticDiagnostic(code=code, message=msg, line=line, is_error=False)
        )

    def _linked(self, a, b):
        """True if an undirected link exists between roles a and b."""
        return (a, b) in self.links or (b, a) in self.links

    def has_errors(self):
        return any(d.is_error for d in self.diagnostics)

    # ── topology ──────────────────────────────────────────────────────────

    def check_role_decl(self, name, low, high=None, line=0):
        """
        Register a role declaration and validate it.

        E-1: duplicate role name
        E-2: count = 0
        E-3: lower bound > upper bound
        """
        if name in self.roles:
            self._err("E-1", f"Duplicate role name '{name}'", line)
            return

        if low == 0 and (high is None or high == 0):
            self._err("E-2", f"Role '{name}' has count 0 — meaningless declaration", line)
            return

        if high is not None and low > high:
            self._err(
                "E-3",
                f"Role '{name}': range {low}..{high} is invalid — lower bound exceeds upper bound",
                line,
            )
            return

        effective_high = high if high is not None else low
        self.roles[name] = (low, effective_high)

    def check_link_decl(self, r1, r2, line=0):
        """
        Register a link declaration and validate it.

        E-4: undeclared roles
        E-6: reflexive link
        W-5: duplicate edge (warning only)
        """
        for role in (r1, r2):
            if role not in self.roles:
                self._err("E-4", f"Link references undeclared role '{role}'", line)

        if r1 == r2:
            self._err("E-6", f"Reflexive link '{r1} -- {r2}' is not allowed", line)
            return

        if self._linked(r1, r2):
            self._warn("W-5", f"Duplicate link '{r1} -- {r2}' — ignored (merged)", line)
            return

        self.links.append((r1, r2))

    # ── routing ───────────────────────────────────────────────────────────

    def check_asn_decl(self, role, asn, line=0):
        """E-14: ASN assigned to undeclared role."""
        if role not in self.roles:
            self._err("E-14", f"ASN {asn} assigned to undeclared role '{role}'", line)

    # ── policy ────────────────────────────────────────────────────────────

    def check_policy_rank(self, policy_name, rank, line=0):
        """E-7: duplicate rank within the same policy."""
        if policy_name not in self.policies:
            self.policies[policy_name] = []

        if rank in self.policies[policy_name]:
            self._err(
                "E-7",
                f"Duplicate rank {rank} in policy '{policy_name}' — each rank must be unique",
                line,
            )
        else:
            self.policies[policy_name].append(rank)

    def finalize_policy(self, policy_name, line=0):
        """Called when all stanzas of a policy have been registered."""
        if policy_name not in self.policies:
            self.policies[policy_name] = []

    # ── intent ────────────────────────────────────────────────────────────

    def check_policy_ref(self, policy_ref, context="", line=0):
        """E-8: reference to undefined policy."""
        if policy_ref and policy_ref not in self.policies:
            ctx = f" (in '{context}')" if context else ""
            self._err(
                "E-8",
                f"Undefined policy reference '{policy_ref}'{ctx} — no matching define block",
                line,
            )

    def check_path_expr(self, roles_in_path, context="", line=0):
        """
        Validate a path expression.

        E-10: undeclared role in path
        E-11: consecutive roles not linked in topology
        """
        ctx = f" (in {context})" if context else ""

        for role in roles_in_path:
            if role not in self.roles:
                self._err("E-10", f"Path{ctx} references undeclared role '{role}'", line)

        for i in range(len(roles_in_path) - 1):
            a, b = roles_in_path[i], roles_in_path[i + 1]
            if a in self.roles and b in self.roles:
                if not self._linked(a, b):
                    self._err(
                        "E-11",
                        f"No topology link between consecutive path roles '{a}' and '{b}'{ctx}",
                        line,
                    )

    def check_intent_decl(self, name, primary_path, backup_path, policy_ref, fault_tol, line=0):
        """
        Full validation for a route intent.

        E-9:  duplicate intent name
        E-8:  undefined policy reference
        E-10: undeclared role in path
        E-11: disconnected hop in path
        E-12: backup identical to primary
        E-13: fault-tolerance = 0
        """
        if name in self.intents:
            self._err("E-9", f"Duplicate intent name '{name}'", line)
        else:
            self.intents.add(name)

        if policy_ref:
            self.check_policy_ref(policy_ref, context=name, line=line)

        if fault_tol == 0:
            self._err(
                "E-13",
                f"Intent '{name}': fault-tolerance k=0 is invalid — must be at least 1",
                line,
            )

        if primary_path:
            self.check_path_expr(primary_path, context=f"intent '{name}' primary", line=line)

        if backup_path:
            self.check_path_expr(backup_path, context=f"intent '{name}' backup", line=line)

        if primary_path and backup_path and primary_path == backup_path:
            self._err(
                "E-12",
                f"Intent '{name}': backup path is identical to primary path — no redundancy",
                line,
            )

    # ── reporting ─────────────────────────────────────────────────────────

    def report(self, verbose=False):
        """Return a formatted diagnostic report string."""
        if not self.diagnostics:
            return "  ✔  Semantic analysis passed — no errors or warnings.\n"

        lines = []
        errors   = [d for d in self.diagnostics if d.is_error]
        warnings = [d for d in self.diagnostics if not d.is_error]

        for d in self.diagnostics:
            prefix = "  ✗  " if d.is_error else "  ⚠  "
            lines.append(f"{prefix}{d}")

        lines.append(f"\n  {len(errors)} error(s), {len(warnings)} warning(s) found.")
        return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════════
# ANTLR listener — bridges the parse tree to SemanticChecker
# ═══════════════════════════════════════════════════════════════════════════════

class SemanticCheckerListener(RouterLangListener):
    """
    Walks the ANTLR parse tree and drives SemanticChecker.

    Usage
    -----
        checker  = SemanticChecker()
        listener = SemanticCheckerListener(checker)
        ParseTreeWalker.DEFAULT.walk(listener, tree)
        print(checker.report())
    """

    def __init__(self, checker):
        self.checker         = checker
        self._current_policy = None

    # ── topology ──────────────────────────────────────────────────────────

    def enterRoleDecl(self, ctx):
        name = ctx.IDENT().getText()
        line = ctx.start.line
        ir   = ctx.intRange()
        ints = [int(n.getText()) for n in ir.INT()]
        if len(ints) == 1:
            self.checker.check_role_decl(name, ints[0], None, line)
        else:
            self.checker.check_role_decl(name, ints[0], ints[1], line)

    def enterLinkDecl(self, ctx):
        idents = [i.getText() for i in ctx.IDENT()]
        if len(idents) >= 2:
            self.checker.check_link_decl(idents[0], idents[1], ctx.start.line)

    # ── routing ───────────────────────────────────────────────────────────

    def enterRoleAsn(self, ctx):
        role = ctx.IDENT().getText()
        asn  = int(ctx.INT().getText())
        self.checker.check_asn_decl(role, asn, ctx.start.line)

    # ── policy ────────────────────────────────────────────────────────────

    def enterPolicyDef(self, ctx):
        self._current_policy = ctx.IDENT().getText()

    def enterPolicyStanza(self, ctx):
        rank_ctx = ctx.rankClause()
        if rank_ctx and self._current_policy:
            rank = int(rank_ctx.INT().getText())
            self.checker.check_policy_rank(
                self._current_policy, rank, ctx.start.line
            )

    def exitPolicyDef(self, ctx):
        if self._current_policy:
            self.checker.finalize_policy(self._current_policy, ctx.start.line)
        self._current_policy = None

    # ── intent ────────────────────────────────────────────────────────────

    def enterIntentDecl(self, ctx):
        name = ctx.IDENT(0).getText()
        line = ctx.start.line

        primary, backup = [], []
        policy_ref      = None
        fault_tol       = 1   # safe default

        route_body = ctx.routeBody() if hasattr(ctx, "routeBody") else None
        if route_body is None:
            return

        # primary (and optional backup) path
        path_spec = route_body.pathSpec()
        if path_spec:
            exprs = path_spec.pathExpr()
            if len(exprs) >= 1:
                primary = [i.getText() for i in exprs[0].IDENT()]
            if len(exprs) >= 2:
                backup = [i.getText() for i in exprs[1].IDENT()]

        # policy reference
        pol_ctx = route_body.policyRef()
        if pol_ctx:
            policy_ref = pol_ctx.IDENT().getText()

        # fault-tolerance
        ft_ctx = route_body.ftSpec()
        if ft_ctx:
            fault_tol = int(ft_ctx.INT().getText())

        self.checker.check_intent_decl(
            name, primary, backup, policy_ref, fault_tol, line
        )


# ═══════════════════════════════════════════════════════════════════════════════
# Public entry point
# ═══════════════════════════════════════════════════════════════════════════════

def analyze(source, verbose=False):
    """
    Parse a RouterLang source string and run full semantic analysis.
    Returns a SemanticChecker with populated .diagnostics.
    """
    input_stream = InputStream(source)
    lexer        = RouterLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser       = RouterLangParser(token_stream)
    parser.removeErrorListeners()

    tree     = parser.program()
    checker  = SemanticChecker()
    listener = SemanticCheckerListener(checker)
    ParseTreeWalker.DEFAULT.walk(listener, tree)
    return checker


# ═══════════════════════════════════════════════════════════════════════════════
# Built-in test suite
# ═══════════════════════════════════════════════════════════════════════════════

def _run_tests(verbose=False):
    PASS = [0]
    FAIL = [0]

    GREEN  = "\033[92m"
    RED    = "\033[91m"
    RESET  = "\033[0m"
    BOLD   = "\033[1m"

    def ok(label):
        PASS[0] += 1
        print(f"  {GREEN}✅ PASS{RESET}  {label}")

    def fail(label, detail=""):
        FAIL[0] += 1
        note = f"  — {detail}" if detail else ""
        print(f"  {RED}❌ FAIL{RESET}  {label}{note}")

    def expect_error(checker, code, label):
        codes = [d.code for d in checker.diagnostics if d.is_error]
        if code in codes:
            ok(label)
        else:
            fail(label, f"expected {code}, got: {codes}")

    def expect_warning(checker, code, label):
        codes = [d.code for d in checker.diagnostics if not d.is_error]
        if code in codes:
            ok(label)
        else:
            fail(label, f"expected warning {code}, got: {codes}")

    def expect_clean(checker, label):
        errors = [d for d in checker.diagnostics if d.is_error]
        if not errors:
            ok(label)
        else:
            fail(label, f"unexpected errors: {[str(d) for d in errors]}")

    def base():
        """Two-role topology with policy P pre-registered."""
        c = SemanticChecker()
        c.check_role_decl("r1", 1)
        c.check_role_decl("r2", 1)
        c.check_link_decl("r1", "r2")
        c.policies["P"] = [10]
        return c

    print(f"\n{BOLD}{'═'*60}{RESET}")
    print(f"{BOLD}  RouterLang Semantic Checker — Test Suite{RESET}")
    print(f"{BOLD}{'═'*60}{RESET}\n")

    # ── Topology ──────────────────────────────────────────────────────────
    print(f"{BOLD}── Topology ─────────────────────────────────────────────{RESET}")

    c = SemanticChecker()
    c.check_role_decl("spine", 2)
    expect_clean(c, "T-01  Valid exact-count role")

    c = SemanticChecker()
    c.check_role_decl("leaf", 1, 8)
    expect_clean(c, "T-02  Valid range role (1..8)")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_role_decl("r1", 2)
    expect_error(c, "E-1", "T-03  E-1  Duplicate role name")

    c = SemanticChecker()
    c.check_role_decl("r1", 0)
    expect_error(c, "E-2", "T-04  E-2  Role with count 0")

    c = SemanticChecker()
    c.check_role_decl("r1", 5, 2)
    expect_error(c, "E-3", "T-05  E-3  Inverted range (5..2)")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_role_decl("r2", 1)
    c.check_link_decl("r1", "r2")
    expect_clean(c, "T-06  Valid link between declared roles")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_link_decl("r1", "ghost")
    expect_error(c, "E-4", "T-07  E-4  Link to undeclared role")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_link_decl("r1", "r1")
    expect_error(c, "E-6", "T-08  E-6  Reflexive link")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_role_decl("r2", 1)
    c.check_link_decl("r1", "r2")
    c.check_link_decl("r1", "r2")
    expect_warning(c, "W-5", "T-09  W-5  Duplicate link (warning only)")
    expect_clean(c, "T-09b W-5  Duplicate link is non-fatal")

    # ── Routing / ASN ─────────────────────────────────────────────────────
    print(f"\n{BOLD}── Routing / ASN ────────────────────────────────────────{RESET}")

    c = SemanticChecker()
    c.check_role_decl("spine", 2)
    c.check_asn_decl("spine", 65001)
    expect_clean(c, "R-01  Valid ASN assignment")

    c = SemanticChecker()
    c.check_asn_decl("ghost", 65099)
    expect_error(c, "E-14", "R-02  E-14  ASN to undeclared role")

    # ── Policy ────────────────────────────────────────────────────────────
    print(f"\n{BOLD}── Policy ───────────────────────────────────────────────{RESET}")

    c = SemanticChecker()
    c.check_policy_rank("POL", 10)
    c.check_policy_rank("POL", 20)
    expect_clean(c, "P-01  Valid unique ranks")

    c = SemanticChecker()
    c.check_policy_rank("POL", 10)
    c.check_policy_rank("POL", 10)
    expect_error(c, "E-7", "P-02  E-7  Duplicate rank in policy")

    c = SemanticChecker()
    c.check_policy_rank("POL-A", 10)
    c.check_policy_rank("POL-B", 10)
    expect_clean(c, "P-03  Same rank in different policies (OK)")

    # ── Paths ─────────────────────────────────────────────────────────────
    print(f"\n{BOLD}── Path expressions ─────────────────────────────────────{RESET}")

    c = base()
    c.check_path_expr(["r1", "r2"])
    expect_clean(c, "X-01  Valid two-hop path r1 >> r2")

    c = base()
    c.check_path_expr(["r1", "r2", "r3"])
    expect_error(c, "E-10", "X-02  E-10  Undeclared role in path")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_role_decl("r2", 1)
    c.check_role_decl("r3", 1)
    c.check_link_decl("r1", "r2")
    c.check_path_expr(["r1", "r2", "r3"])
    expect_error(c, "E-11", "X-03  E-11  Disconnected hop in path")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_role_decl("r2", 1)
    c.check_role_decl("r3", 1)
    c.check_link_decl("r1", "r2")
    c.check_link_decl("r2", "r3")
    c.check_path_expr(["r1", "r2", "r3"])
    expect_clean(c, "X-04  Valid three-hop path r1 >> r2 >> r3")

    # ── Intent ────────────────────────────────────────────────────────────
    print(f"\n{BOLD}── Intent declarations ──────────────────────────────────{RESET}")

    c = base()
    c.check_intent_decl("I1", ["r1", "r2"], [], "P", 1)
    expect_clean(c, "I-01  Valid route intent")

    c = base()
    c.check_intent_decl("I1", ["r1", "r2"], [], "P", 1)
    c.check_intent_decl("I1", ["r1", "r2"], [], "P", 1)
    expect_error(c, "E-9", "I-02  E-9  Duplicate intent name")

    c = base()
    c.check_intent_decl("I1", ["r1", "r2"], [], "MISSING", 1)
    expect_error(c, "E-8", "I-03  E-8  Undefined policy reference")

    c = base()
    c.check_intent_decl("I1", ["r1", "r2"], ["r1", "r2"], "P", 1)
    expect_error(c, "E-12", "I-04  E-12  Backup == primary path")

    c = base()
    c.check_intent_decl("I1", ["r1", "r2"], [], "P", 0)
    expect_error(c, "E-13", "I-05  E-13  fault-tolerance k=0")

    c = SemanticChecker()
    c.check_role_decl("r1", 1)
    c.check_role_decl("r2", 1)
    c.check_role_decl("r3", 1)
    c.check_link_decl("r1", "r2")
    c.check_link_decl("r2", "r3")
    c.check_link_decl("r1", "r3")
    c.policies["P"] = [10]
    c.check_intent_decl("I1", ["r1", "r2", "r3"], ["r1", "r3"], "P", 1)
    expect_clean(c, "I-06  Valid intent with distinct backup path")

    # ── Integration: ANTLR parse-tree walk ────────────────────────────────
    print(f"\n{BOLD}── Integration (ANTLR listener) ──────────────────────────{RESET}")

    VALID = """
topology {
  roles {
    spine  { count: 2 }
    leaf   { count: 1..8 }
    edge   { count: 2 }
  }
  links {
    spine  -- leaf
    spine  -- edge
    edge   -- leaf
  }
}
routing {
  bgp {
    asn { spine: 65001  leaf: 65002  edge: 65003 }
    neighbors: auto
  }
}
policy {
  define MAIN {
    rank 10: permit { match prefix 10.0.0.0/8 le 24  set local-pref 200 }
    rank 20: deny   { match any }
  }
}
intent {
  CORE: route backbone {
    primary: edge >> spine >> leaf
    backup:  edge >> leaf
    apply-policy: MAIN
    fault-tolerance: 1
    scope: all
  }
}
"""
    try:
        c = analyze(VALID)
        expect_clean(c, "A-01  Full valid program via ANTLR")
    except Exception as e:
        fail("A-01  Full valid program via ANTLR", str(e))

    DUPE_ROLE = """
topology {
  roles { r1 { count: 1 }  r1 { count: 2 } }
  links { r1 -- r1 }
}
routing { bgp { asn { r1: 65001 } neighbors: auto } }
policy { define P { permit { match any } } }
intent { I1: route t { primary: r1 >> r1 } }
"""
    try:
        c = analyze(DUPE_ROLE)
        expect_error(c, "E-1", "A-02  E-1  Duplicate role via ANTLR")
    except Exception as e:
        fail("A-02  E-1  Duplicate role via ANTLR", str(e))

    MISSING_POL = """
topology {
  roles { r1 { count: 1 }  r2 { count: 1 } }
  links { r1 -- r2 }
}
routing { bgp { asn { r1: 65001  r2: 65002 } neighbors: auto } }
policy { define P { permit { match any } } }
intent {
  I1: route t {
    primary: r1 >> r2
    apply-policy: NONEXISTENT
  }
}
"""
    try:
        c = analyze(MISSING_POL)
        expect_error(c, "E-8", "A-03  E-8  Undefined policy ref via ANTLR")
    except Exception as e:
        fail("A-03  E-8  Undefined policy ref via ANTLR", str(e))

    UNLINKED = """
topology {
  roles { r1 { count: 1 }  r2 { count: 1 }  r3 { count: 1 } }
  links { r1 -- r2 }
}
routing { bgp { asn { r1: 65001  r2: 65002  r3: 65003 } neighbors: auto } }
policy { define P { permit { match any } } }
intent {
  I1: route t {
    primary: r1 >> r2 >> r3
    apply-policy: P
  }
}
"""
    try:
        c = analyze(UNLINKED)
        expect_error(c, "E-11", "A-04  E-11  Disconnected path hop via ANTLR")
    except Exception as e:
        fail("A-04  E-11  Disconnected path hop via ANTLR", str(e))

    DUPE_RANK = """
topology {
  roles { r1 { count: 1 }  r2 { count: 1 } }
  links { r1 -- r2 }
}
routing { bgp { asn { r1: 65001  r2: 65002 } neighbors: auto } }
policy {
  define P {
    rank 10: permit { match any }
    rank 10: deny   { match any }
  }
}
intent { I1: route t { primary: r1 >> r2  apply-policy: P } }
"""
    try:
        c = analyze(DUPE_RANK)
        expect_error(c, "E-7", "A-05  E-7  Duplicate rank via ANTLR")
    except Exception as e:
        fail("A-05  E-7  Duplicate rank via ANTLR", str(e))

    # ── Summary ───────────────────────────────────────────────────────────
    total = PASS[0] + FAIL[0]
    colour = GREEN if FAIL[0] == 0 else RED
    print(f"\n{BOLD}{'═'*60}{RESET}")
    print(f"{BOLD}  Results: {colour}{PASS[0]}/{total} passed{RESET}")
    if FAIL[0] > 0:
        print(f"{RED}  {FAIL[0]} test(s) FAILED{RESET}")
    print(f"{BOLD}{'═'*60}{RESET}\n")
    return FAIL[0] == 0


if __name__ == "__main__":
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    ok = _run_tests(verbose=verbose)
    sys.exit(0 if ok else 1)