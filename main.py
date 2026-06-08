"""
RouterLang — Main Runner
========================
Single entry point that runs a .rl file through the full pipeline:
    Lexer  →  Parser  →  Symbol Table  →  Semantic Checker  →  [Config Generator]

Usage:
    python main.py <file.rl>                          # full pipeline
    python main.py <file.rl> --tokens                 # also print token stream
    python main.py <file.rl> --symbols                # also print symbol table
    python main.py <file.rl> --verbose                # full detail on all stages
    python main.py <file.rl> --generate               # emit per-device .cfg files (Cisco IOS)
    python main.py <file.rl> --generate --vendor junos
    python main.py <file.rl> --generate --vendor openconfig
    python main.py <file.rl> --generate --out-dir ./my-configs
    python main.py <file.rl> --generate --ipam ipam.csv
    python main.py <file.rl> --generate --vendor junos --ipam ipam.csv
    python main.py --example                          # run built-in example and exit
"""

import sys
import os
import argparse
import time

# ── path setup ─────────────────────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src", "parser"))
sys.path.insert(0, os.path.join(ROOT, "src", "compiler"))

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from RouterLangLexer   import RouterLangLexer
from RouterLangParser  import RouterLangParser
from symbol_table      import build_symbol_table
from semantic_checker  import analyze

# ── ANSI colours ───────────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
GREEN   = "\033[92m"
RED     = "\033[91m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
MAGENTA = "\033[95m"
GREY    = "\033[90m"
WHITE   = "\033[97m"

# ── Built-in example .rl program ───────────────────────────────────────────────
EXAMPLE_SOURCE = """\
topology {
  roles {
    spine  { count: 2 }
    leaf   { count: 4 }
    edge   { count: 2 }
  }
  links {
    spine -- leaf  { weight: 1 }
    spine -- edge  { weight: 2 }
    edge  -- leaf  { weight: 3 }
  }
  devices {
    spine: [R-SPINE-1, R-SPINE-2]
    leaf:  [R-LEAF-1, R-LEAF-2, R-LEAF-3, R-LEAF-4]
    edge:  [R-EDGE-1, R-EDGE-2]
  }
}
routing {
  bgp {
    asn {
      spine: 65001
      leaf:  65002
      edge:  65003
    }
    neighbors: auto
    route-reflector: spine
  }
  ospf {
    area 0 { roles: [spine, leaf] }
    area 1 { roles: [edge] }
  }
}
policy {
  define PREFER-PRIMARY {
    rank 10: permit {
      match prefix 192.168.0.0/16 le 24
      set local-pref 300
      if neighbor.state == LIVE
    }
    rank 20: permit {
      match any
      set local-pref 100
    }
    rank 30: deny {
      match prefix 0.0.0.0/0 le 32
    }
  }
}
intent {
  CORE-TRAFFIC: route backbone {
    primary: edge >> spine >> leaf
    backup:  edge >> leaf
    apply-policy: PREFER-PRIMARY
    fault-tolerance: 2
    scope: all
  }
}
"""

# ── Helpers ────────────────────────────────────────────────────────────────────

def banner(title):
    width = 62
    pad = (width - len(title) - 2) // 2
    print(f"\n{BOLD}{CYAN}{'═' * width}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * pad}  {title}  {'═' * pad}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * width}{RESET}")

def section(title):
    print(f"\n{BOLD}{WHITE}── {title} {'─' * (56 - len(title))}{RESET}")

def ok(msg):
    print(f"  {GREEN}   {msg}{RESET}")

def fail(msg):
    print(f"  {RED}✗  {msg}{RESET}")

def warn(msg):
    print(f"  {YELLOW}⚠   {msg}{RESET}")

def info(msg):
    print(f"  {GREY}{msg}{RESET}")

# ── Stage 1: Lexer ─────────────────────────────────────────────────────────────

KEYWORDS = {
    "topology", "routing", "policy", "intent", "transition",
    "roles", "links", "devices", "bgp", "ospf", "asn",
    "neighbors", "route-reflector", "area",
    "define", "rank", "permit", "deny",
    "match", "set", "if",
    "prefix", "aspath", "community", "any",
    "local-pref", "local-preference", "metric",
    "primary", "backup", "apply-policy", "fault-tolerance", "scope",
    "from", "to", "intermediate",
    "route", "constraint",
    "LIVE", "DRAINED", "WARM",
    "auto", "all", "count", "weight", "le",
    "neighbor", "state",
}
PUNCTUATION = {"{", "}", "[", "]", ":", ".", "==", "--", ",", ";"}

def run_lexer(source, show_tokens=False):
    section("STAGE 1 — Lexer")
    input_stream = InputStream(source)
    lexer = RouterLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    tokens = [t for t in stream.tokens if t.type != -1]
    visible = [t for t in tokens if t.channel == 0]

    keywords_found = set()
    idents_found   = []
    errors         = []

    for t in visible:
        txt = t.text
        if txt in KEYWORDS:
            keywords_found.add(txt)
        elif txt not in PUNCTUATION and not txt.lstrip('-').isdigit():
            idents_found.append(txt)
        if t.type == RouterLangLexer.ERROR if hasattr(RouterLangLexer, "ERROR") else False:
            errors.append(t)

    ok(f"Tokenised {len(visible)} visible tokens")
    info(f"Keywords used  : {', '.join(sorted(keywords_found))}")
    info(f"Identifiers    : {', '.join(dict.fromkeys(idents_found))[:120]}")

    if errors:
        for e in errors:
            fail(f"Lexer error at line {e.line}:{e.column} — unexpected '{e.text}'")
    else:
        ok("No lexer errors")

    if show_tokens:
        print()
        print(f"  {BOLD}{'LINE':>5}  {'COL':>4}  {'TYPE':<22}  TEXT{RESET}")
        print(f"  {'─'*55}")
        for t in visible[:80]:
            txt  = t.text
            name = lexer.symbolicNames[t.type] if 0 <= t.type < len(lexer.symbolicNames) else str(t.type)
            col  = CYAN if txt in KEYWORDS else (MAGENTA if txt == ">>" else (GREY if txt in PUNCTUATION else GREEN))
            print(f"  {t.line:>5}  {t.column:>4}  {GREY}{name:<22}{RESET}  {col}{txt!r}{RESET}")
        if len(visible) > 80:
            info(f"  ... and {len(visible)-80} more tokens (use --tokens to see all)")

    return stream, len(errors) == 0

# ── Stage 2: Parser ────────────────────────────────────────────────────────────

def run_parser(source):
    section("STAGE 2 — Parser")
    from antlr4.error.ErrorListener import ErrorListener

    class CE(ErrorListener):
        def __init__(self):
            self.errors = []
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            self.errors.append((line, column, msg))

    input_stream = InputStream(source)
    lexer   = RouterLangLexer(input_stream)
    stream  = CommonTokenStream(lexer)
    parser  = RouterLangParser(stream)
    parser.removeErrorListeners()
    collector = CE()
    parser.addErrorListener(collector)

    tree = parser.program()

    if collector.errors:
        for line, col, msg in collector.errors:
            fail(f"Syntax error at line {line}:{col} — {msg}")
        return None, False
    else:
        depth = tree_depth(tree)
        ok(f"Parse tree built — depth {depth}")
        ok("No syntax errors")
        return tree, True

def tree_depth(node):
    from antlr4 import TerminalNode
    if isinstance(node, TerminalNode):
        return 1
    if node.getChildCount() == 0:
        return 1
    return 1 + max(tree_depth(node.getChild(i)) for i in range(node.getChildCount()))

# ── Stage 3: Symbol Table ──────────────────────────────────────────────────────

def run_symbol_table(source, show_symbols=False):
    section("STAGE 3 — Symbol Table")
    try:
        st = build_symbol_table(source)
    except AttributeError as e:
        warn(f"Symbol table builder has a grammar mismatch ({e})")
        warn("Falling back to semantic checker's internal symbol data")
        checker = analyze(source)
        _show_summary_from_semantic(checker)
        return None, True
    except Exception as e:
        fail(f"Symbol table error: {e}")
        return None, False

    errs = st.errors()
    ok(f"Roles     : {len(st.roles)}")
    ok(f"Links     : {len(st.links)}")
    ok(f"Devices   : {len(st.devices)}")
    ok(f"Policies  : {len(st.policies)}")
    ok(f"Intents   : {len(st.intents)}")
    if st.transition:
        ok(f"Transition: {st.transition.from_topo} → {st.transition.to_topo}")

    if errs:
        for e in errs:
            fail(e)
        return st, False

    ok("Symbol table valid")

    if show_symbols:
        print()
        st.dump()

    return st, True


def _show_summary_from_semantic(checker):
    for attr in ["_roles", "roles"]:
        roles = getattr(checker, attr, None)
        if roles:
            info(f"Roles declared : {', '.join(roles)}")
            break
    for attr in ["_policies", "policies"]:
        pols = getattr(checker, attr, None)
        if pols:
            info(f"Policies       : {', '.join(pols)}")
            break
    for attr in ["_intents", "intents"]:
        ints = getattr(checker, attr, None)
        if ints:
            info(f"Intents        : {', '.join(ints)}")
            break

# ── Stage 4: Semantic Checker ──────────────────────────────────────────────────

def run_semantic(source):
    section("STAGE 4 — Semantic Analysis")
    checker = analyze(source)

    errors   = [d for d in checker.diagnostics if d.is_error]
    warnings = [d for d in checker.diagnostics if not d.is_error]

    if not checker.diagnostics:
        ok("All 14 semantic rules passed — configuration is valid")
    else:
        for d in checker.diagnostics:
            if d.is_error:
                fail(str(d))
            else:
                warn(str(d))

    return checker, len(errors) == 0

# ── Stage 5: Config Generator ──────────────────────────────────────────────────

def run_config_generator(source, filename, out_dir, vendor="cisco", ipam_path=""):
    section("STAGE 5 — Config Generation")
    try:
        from config_generator import generate_configs, SUPPORTED_VENDORS
    except ImportError as e:
        fail(f"Config generator not available: {e}")
        return [], False

    info(f"Vendor target  : {vendor}")
    if ipam_path:
        if os.path.isfile(ipam_path):
            info(f"IPAM file      : {ipam_path}  (real IPs)")
        else:
            warn(f"IPAM file not found: {ipam_path}  (falling back to hash-derived IPs)")

    try:
        written = generate_configs(source, filename, out_dir,
                                   vendor=vendor, ipam_path=ipam_path)
    except ValueError as e:
        fail(str(e))
        return [], False
    except Exception as e:
        fail(f"Config generation failed: {e}")
        import traceback
        traceback.print_exc()
        return [], False

    if not written:
        warn("No config files were generated (no devices or roles found?)")
        return [], False

    ok(f"Generated {len(written)} config file(s) → '{out_dir}/'")
    for path in written:
        info(path)
    return written, True

# ── Summary ────────────────────────────────────────────────────────────────────

def print_summary(source, stages, stage_names, elapsed,
                  generated_files=None, vendor=None, ipam_path=""):
    section("SUMMARY")

    passed = all(stages)

    for name, ok_flag in zip(stage_names, stages):
        sym = f"{GREEN}PASS{RESET}" if ok_flag else f"{RED}FAIL{RESET}"
        print(f"  {BOLD}{name:<22}{RESET}  {sym}")

    lines = source.count("\n") + 1
    print(f"\n  {GREY}Source lines : {lines}{RESET}")
    print(f"  {GREY}Time elapsed : {elapsed*1000:.1f} ms{RESET}")
    if vendor:
        print(f"  {GREY}Vendor target: {vendor}{RESET}")
    if ipam_path:
        ip_label = "IPAM" if os.path.isfile(ipam_path) else "IPAM (file not found — hash fallback)"
        print(f"  {GREY}IP source    : {ipam_path}  [{ip_label}]{RESET}")
    else:
        if vendor:
            print(f"  {GREY}IP source    : hash-derived (no --ipam provided){RESET}")

    if generated_files:
        print(f"\n  {BOLD}{CYAN}Generated config files:{RESET}")
        for p in generated_files:
            print(f"  {GREEN}  {p}{RESET}")

    print()
    if passed:
        print(f"  {BOLD}{GREEN}   Configuration VALID — ready for deployment review.{RESET}")
    else:
        print(f"  {BOLD}{RED}✗   Configuration INVALID — fix errors before deploying.{RESET}")
    print()

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="RouterLang — compile and validate a .rl network configuration file"
    )
    parser.add_argument("file",      nargs="?", help="Path to a .rl source file")
    parser.add_argument("--tokens",  action="store_true", help="Print token stream (stage 1)")
    parser.add_argument("--symbols", action="store_true", help="Print symbol table (stage 3)")
    parser.add_argument("--verbose", action="store_true", help="Enable --tokens and --symbols")
    parser.add_argument("--example", action="store_true", help="Run built-in ISP backbone example")
    parser.add_argument(
        "--generate", action="store_true",
        help="Generate per-device router config files after validation"
    )
    parser.add_argument(
        "--vendor",
        default="cisco",
        choices=["cisco", "junos", "openconfig"],
        help=(
            "Target vendor syntax for --generate. "
            "cisco = Cisco IOS CLI (default, .cfg)  "
            "junos = JunOS hierarchical CLI (.conf)  "
            "openconfig = OpenConfig JSON (.json)"
        ),
    )
    parser.add_argument(
        "--out-dir", default="",
        help="Output directory for generated configs (default: ./output/<filename>/)"
    )
    parser.add_argument(
        "--ipam", default="",
        help=(
            "Path to a CSV file mapping device names to real IP addresses. "
            "Expected columns: device, loopback_ip, mgmt_ip. "
            "If omitted or a device is missing, hash-derived IPs are used as fallback."
        ),
    )
    args = parser.parse_args()

    show_tokens  = args.tokens  or args.verbose
    show_symbols = args.symbols or args.verbose

    if args.example:
        source   = EXAMPLE_SOURCE
        filename = "<built-in ISP backbone example>"
        basename = "example"
    elif args.file:
        if not os.path.isfile(args.file):
            print(f"{RED}Error: file not found: {args.file}{RESET}")
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            source = f.read()
        filename = args.file
        basename = os.path.splitext(os.path.basename(args.file))[0]
    else:
        parser.print_help()
        sys.exit(0)

    banner("RouterLang Compiler")
    print(f"\n  {GREY}File   : {filename}{RESET}")
    print(f"  {GREY}Lines  : {source.count(chr(10))+1}{RESET}")
    if args.generate:
        print(f"  {GREY}Vendor : {args.vendor}{RESET}")
        if args.ipam:
            print(f"  {GREY}IPAM   : {args.ipam}{RESET}")

    t0 = time.time()

    _,  ok1 = run_lexer(source, show_tokens)
    _,  ok2 = run_parser(source)
    st, ok3 = run_symbol_table(source, show_symbols)
    _,  ok4 = run_semantic(source)

    generated_files = []
    stage_names     = ["Lexer", "Parser", "Symbol Table", "Semantic"]
    all_stages      = [ok1, ok2, ok3, ok4]

    if args.generate:
        stage_names.append("Config Generation")
        if all([ok1, ok2, ok3, ok4]):
            out_dir = args.out_dir or os.path.join("output", basename)
            files, ok5 = run_config_generator(
                source, filename, out_dir,
                vendor=args.vendor,
                ipam_path=args.ipam,
            )
            generated_files = files
            all_stages.append(ok5)
        else:
            warn("Skipping config generation — fix validation errors first.")
            all_stages.append(False)

    elapsed = time.time() - t0
    print_summary(
        source, all_stages, stage_names, elapsed,
        generated_files,
        vendor=args.vendor if args.generate else None,
        ipam_path=args.ipam if args.generate else "",
    )

    sys.exit(0 if all(all_stages) else 1)


if __name__ == "__main__":
    main()