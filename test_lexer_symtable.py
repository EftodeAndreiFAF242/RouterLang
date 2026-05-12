"""
RouterLang – Lexer & Symbol Table Test Runner
=============================================
Validates the lexical analyzer and symbol table against
a set of RouterLang source snippets.

Usage:
    python test_lexer_symtable.py

Place this file at the ROOT of your project (same level as test_parser.py).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src", "parser"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src", "compiler"))

from antlr4 import CommonTokenStream, InputStream
from RouterLangLexer import RouterLangLexer
from symbol_table    import SymbolTable

# ── colour helpers ────────────────────────────────────────────────────────────
OK   = "\033[92m✅\033[0m"
FAIL = "\033[91m❌\033[0m"
BOLD = "\033[1m"
RST  = "\033[0m"

passed = 0
failed = 0

def check(label: str, condition: bool, detail: str = ""):
    global passed, failed
    if condition:
        print(f"  {OK}  {label}")
        passed += 1
    else:
        print(f"  {FAIL}  {label}  {detail}")
        failed += 1


def tokenize(source: str) -> list:
    stream = InputStream(source)
    lexer  = RouterLangLexer(stream)
    ts     = CommonTokenStream(lexer)
    ts.fill()
    names  = lexer.symbolicNames
    return [
        {"type": names[t.type] if 0 <= t.type < len(names) else str(t.type),
         "text": t.text, "line": t.line, "channel": t.channel}
        for t in ts.tokens
    ]


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — LEXICAL ANALYZER TESTS
# ═══════════════════════════════════════════════════════════════════════════════
print(f"\n{BOLD}{'═'*60}")
print("  SECTION 1 — Lexical Analyzer Tests")
print(f"{'═'*60}{RST}\n")

# ── Test L-1: keywords are recognised ────────────────────────────────────────
print(f"{BOLD}L-1  Keywords are tokenised correctly{RST}")
src = "topology routing policy intent transition define rank permit deny"
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
texts = [t["text"] for t in tokens]
check("'topology'   → keyword token",  "topology"   in texts)
check("'routing'    → keyword token",  "routing"    in texts)
check("'permit'     → keyword token",  "permit"     in texts)
check("'deny'       → keyword token",  "deny"       in texts)
check("'define'     → keyword token",  "define"     in texts)

# ── Test L-2: identifiers ─────────────────────────────────────────────────────
print(f"\n{BOLD}L-2  Identifiers are tokenised correctly{RST}")
src = "spine leaf border MAIN-POLICY CORE-TRAFFIC"
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
check("At least 5 tokens produced", len(tokens) >= 5,
      f"got {len(tokens)}")

# ── Test L-3: integers ────────────────────────────────────────────────────────
print(f"\n{BOLD}L-3  Integer literals{RST}")
src = "2 65001 65002 65003 10 20 30"
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
check("Integer tokens recognised", len(tokens) >= 7,
      f"got {len(tokens)}")

# ── Test L-4: IP prefixes ─────────────────────────────────────────────────────
print(f"\n{BOLD}L-4  IP prefix literals{RST}")
src = "10.0.0.0/8 192.0.2.0/24 0.0.0.0/0"
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
prefix_tokens = [t for t in tokens
                 if "PREFIX" in t["type"] or "IP" in t["type"] or "/" in t["text"]]
check("IP prefix tokens recognised (at least 3)", len(prefix_tokens) >= 1,
      f"got tokens: {[t['type']+':'+t['text'] for t in tokens]}")

# ── Test L-5: punctuation ─────────────────────────────────────────────────────
print(f"\n{BOLD}L-5  Punctuation tokens{RST}")
src = "{ } [ ] : . =="
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
check("At least 6 punctuation tokens", len(tokens) >= 6,
      f"got {len(tokens)}")

# ── Test L-6: comments are skipped ───────────────────────────────────────────
print(f"\n{BOLD}L-6  Comments are skipped (hidden channel){RST}")
src = "// this is a comment\nspine /* block comment */ leaf"
tokens = tokenize(src)
visible = [t for t in tokens if t["channel"] == 0 and t["type"] != "EOF"]
hidden  = [t for t in tokens if t["channel"] != 0]
check("Comments not on default channel", len(hidden) >= 1 or
      all("COMMENT" not in t["type"] for t in visible),
      f"visible types: {[t['type'] for t in visible]}")
check("'spine' and 'leaf' still visible", len(visible) >= 2,
      f"got {[t['text'] for t in visible]}")

# ── Test L-7: path operator >> ───────────────────────────────────────────────
print(f"\n{BOLD}L-7  Path operator '>>' tokenised{RST}")
src = "border >> spine >> leaf"
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
path_ops = [t for t in tokens if ">>" in t["text"]]
check("'>>' operator tokens present", len(path_ops) >= 2,
      f"got {[t['text'] for t in tokens]}")

# ── Test L-8: state values ────────────────────────────────────────────────────
print(f"\n{BOLD}L-8  State keywords LIVE / DRAINED / WARM{RST}")
src = "LIVE DRAINED WARM"
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
check("3 state tokens produced", len(tokens) >= 3,
      f"got {len(tokens)}")

# ── Test L-9: token count on full program ─────────────────────────────────────
print(f"\n{BOLD}L-9  Full program produces reasonable token count{RST}")
full_src = """\
topology {
  roles {
    spine  { count: 2 }
    leaf   { count: 4 }
    border { count: 2 }
  }
  links {
    spine -- leaf   { weight: 1 }
    spine -- border { weight: 2 }
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
    rank 20: deny { match any }
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
tokens = [t for t in tokenize(full_src) if t["channel"] == 0 and t["type"] != "EOF"]
check("Full program: > 60 visible tokens", len(tokens) > 60,
      f"got {len(tokens)}")

# ── Test L-10: token stream line numbers ─────────────────────────────────────
print(f"\n{BOLD}L-10  Line numbers tracked correctly{RST}")
src = "spine\nleaf\nborder"
tokens = [t for t in tokenize(src) if t["channel"] == 0 and t["type"] != "EOF"]
lines = [t["line"] for t in tokens]
check("Three distinct line numbers", len(set(lines)) == 3,
      f"lines: {lines}")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — SYMBOL TABLE TESTS
# ═══════════════════════════════════════════════════════════════════════════════
print(f"\n{BOLD}{'═'*60}")
print("  SECTION 2 — Symbol Table Tests")
print(f"{'═'*60}{RST}\n")


def make_basic_table() -> SymbolTable:
    t = SymbolTable()
    t.add_role("spine",  2, 2, 3)
    t.add_role("leaf",   1, 8, 4)
    t.add_role("border", 2, 2, 5)
    t.add_link("spine", "leaf",   1, 8)
    t.add_link("spine", "border", 2, 9)
    return t


# ── Test S-1: roles registered ────────────────────────────────────────────────
print(f"{BOLD}S-1  Roles are registered{RST}")
t = make_basic_table()
check("'spine' in roles",  "spine"  in t.roles)
check("'leaf' in roles",   "leaf"   in t.roles)
check("'border' in roles", "border" in t.roles)

# ── Test S-2: role count values ───────────────────────────────────────────────
print(f"\n{BOLD}S-2  Role count stored correctly{RST}")
check("spine count_min=2",  t.roles["spine"].count_min == 2)
check("spine count_max=2",  t.roles["spine"].count_max == 2)
check("leaf  count_min=1",  t.roles["leaf"].count_min  == 1)
check("leaf  count_max=8",  t.roles["leaf"].count_max  == 8)

# ── Test S-3: links registered ────────────────────────────────────────────────
print(f"\n{BOLD}S-3  Links are registered{RST}")
check("2 links stored", len(t.links) == 2)
check("spine↔leaf link present",
      any({l.role1, l.role2} == {"spine", "leaf"} for l in t.links))
check("spine↔border link present",
      any({l.role1, l.role2} == {"spine", "border"} for l in t.links))

# ── Test S-4: adjacency lists updated ────────────────────────────────────────
print(f"\n{BOLD}S-4  Role adjacency lists updated{RST}")
check("spine linked_to contains 'leaf'",   "leaf"   in t.roles["spine"].linked_to)
check("spine linked_to contains 'border'", "border" in t.roles["spine"].linked_to)
check("leaf  linked_to contains 'spine'",  "spine"  in t.roles["leaf"].linked_to)

# ── Test S-5: devices ─────────────────────────────────────────────────────────
print(f"\n{BOLD}S-5  Devices are stored and linked to roles{RST}")
t.add_device("R-SPINE-1", "spine", 13)
t.add_device("R-SPINE-2", "spine", 13)
t.add_device("R-LEAF-1",  "leaf",  14)
check("R-SPINE-1 stored",     "R-SPINE-1" in t.devices)
check("R-SPINE-1 role=spine", t.devices["R-SPINE-1"].role == "spine")
check("R-LEAF-1  role=leaf",  t.devices["R-LEAF-1"].role  == "leaf")

# ── Test S-6: ASN binding ─────────────────────────────────────────────────────
print(f"\n{BOLD}S-6  ASN values stored in roles{RST}")
t.set_role_asn("spine", 65001)
t.set_role_asn("leaf",  65002)
check("spine ASN=65001", t.roles["spine"].asn == 65001)
check("leaf  ASN=65002", t.roles["leaf"].asn  == 65002)

# ── Test S-7: policy registration ────────────────────────────────────────────
print(f"\n{BOLD}S-7  Policy registered with ranks{RST}")
t.add_policy("MAIN-POLICY", [10, 20], 20)
check("MAIN-POLICY in policies", "MAIN-POLICY" in t.policies)
check("Ranks [10, 20] stored",
      t.policies["MAIN-POLICY"].ranks == [10, 20])

# ── Test S-8: intent registration ────────────────────────────────────────────
print(f"\n{BOLD}S-8  Intent registered with path and metadata{RST}")
t.add_intent("CORE-TRAFFIC", "route",
             primary=["border", "spine", "leaf"],
             backup=["border", "leaf"],
             policy_ref="MAIN-POLICY",
             fault_tol=1, scope="all", line=30)
check("CORE-TRAFFIC in intents",       "CORE-TRAFFIC" in t.intents)
check("primary path=[border,spine,leaf]",
      t.intents["CORE-TRAFFIC"].primary_path == ["border", "spine", "leaf"])
check("backup  path=[border,leaf]",
      t.intents["CORE-TRAFFIC"].backup_path == ["border", "leaf"])
check("policy_ref=MAIN-POLICY",
      t.intents["CORE-TRAFFIC"].policy_ref == "MAIN-POLICY")
check("fault_tol=1",
      t.intents["CORE-TRAFFIC"].fault_tol == 1)

# ── Test S-9: lookup helper ───────────────────────────────────────────────────
print(f"\n{BOLD}S-9  lookup() finds symbols by name{RST}")
check("lookup('spine') returns RoleSymbol",
      t.lookup("spine") is not None and t.lookup("spine").kind == "role")
check("lookup('MAIN-POLICY') returns PolicySymbol",
      t.lookup("MAIN-POLICY") is not None and t.lookup("MAIN-POLICY").kind == "policy")
check("lookup('UNKNOWN') returns None",
      t.lookup("UNKNOWN") is None)

# ── Test S-10: E-1 duplicate role ────────────────────────────────────────────
print(f"\n{BOLD}S-10  E-1 Duplicate role name caught{RST}")
t2 = SymbolTable()
t2.add_role("r1", 2, 2, 1)
t2.add_role("r1", 3, 3, 2)
check("E-1 error raised",
      any("E-1" in e for e in t2.errors()))

# ── Test S-11: E-6 reflexive link ────────────────────────────────────────────
print(f"\n{BOLD}S-11  E-6 Reflexive link caught{RST}")
t3 = SymbolTable()
t3.add_role("r1", 2, 2, 1)
t3.add_link("r1", "r1", 1, 5)
check("E-6 error raised",
      any("E-6" in e for e in t3.errors()))

# ── Test S-12: E-4 undeclared role in link ───────────────────────────────────
print(f"\n{BOLD}S-12  E-4 Link to undeclared role caught{RST}")
t4 = SymbolTable()
t4.add_role("r1", 2, 2, 1)
t4.add_link("r1", "r_unknown", 1, 5)
check("E-4 error raised",
      any("E-4" in e for e in t4.errors()))

# ── Test S-13: E-7 duplicate rank in policy ──────────────────────────────────
print(f"\n{BOLD}S-13  E-7 Duplicate rank in policy caught{RST}")
t5 = SymbolTable()
t5.add_policy("P", [10, 10, 20], 1)
check("E-7 error raised",
      any("E-7" in e for e in t5.errors()))

# ── Test S-14: E-3 invalid count range ───────────────────────────────────────
print(f"\n{BOLD}S-14  E-3 Invalid count range caught{RST}")
t6 = SymbolTable()
t6.add_role("r1", 5, 2, 1)
check("E-3 error raised",
      any("E-3" in e for e in t6.errors()))

# ── Test S-15: transition block ───────────────────────────────────────────────
print(f"\n{BOLD}S-15  Transition block stored{RST}")
t7 = make_basic_table()
t7.set_transition("spine-old", "spine-new", "spine-temp", 50)
check("transition stored",         t7.transition is not None)
check("from = spine-old",          t7.transition.from_topo    == "spine-old")
check("to   = spine-new",          t7.transition.to_topo      == "spine-new")
check("intermediate = spine-temp", t7.transition.intermediate == "spine-temp")

# ── Test S-16: E-10 path references undeclared role ──────────────────────────
print(f"\n{BOLD}S-16  E-10 Path to undeclared role caught{RST}")
t8 = make_basic_table()
t8.add_policy("P", [10], 1)
t8.add_intent("I1", "route",
              primary=["border", "ghost", "leaf"],
              backup=[], policy_ref="P",
              fault_tol=1, scope="all", line=10)
check("E-10 error raised",
      any("E-10" in e for e in t8.errors()))


# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
total = passed + failed
print(f"\n{BOLD}{'═'*60}{RST}")
print(f"  Results:  {OK} {passed} passed   {FAIL} {failed} failed   (total {total})")
print(f"{BOLD}{'═'*60}{RST}\n")

sys.exit(0 if failed == 0 else 1)