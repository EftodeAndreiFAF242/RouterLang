"""
RouterLang Lexical Analyzer
===========================
Reads a .rl source file and prints a formatted token stream
with: line, column, token type name, and raw text.

Usage:
    python lexer_analyzer.py examples/sample_network.rl
    python lexer_analyzer.py                          # runs built-in demo
    python lexer_analyzer.py --summary                # show token counts
    python lexer_analyzer.py --hidden                 # show whitespace tokens

Place this file at the ROOT of your RouterLang project (same level as test_parser.py).
"""

import sys
import os

# ── make sure the generated parser is on the path ─────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src", "parser"))

from antlr4 import CommonTokenStream, FileStream, InputStream
from RouterLangLexer import RouterLangLexer

# ── ANSI colours ──────────────────────────────────────────────────────────────
RESET          = "\033[0m"
CYAN           = "\033[96m"
YELLOW         = "\033[93m"
GREEN          = "\033[92m"
RED            = "\033[91m"
GREY           = "\033[90m"
BOLD           = "\033[1m"
MAGENTA        = "\033[95m"

KEYWORD_COLOUR = CYAN
LITERAL_COLOUR = YELLOW
PUNCT_COLOUR   = GREY
ERROR_COLOUR   = RED
IDENT_COLOUR   = GREEN
PATH_COLOUR    = MAGENTA

# ── All RouterLang keywords (matched against token TEXT) ─────────────────────
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


def friendly_name(token_type: int, text: str, symbolic_names: list) -> str:
    """
    Convert a raw token type integer to a human-readable name.
    Falls back to guessing from the text if the symbolic name is unhelpful.
    """
    # Try the lexer's own symbolic name first
    if 0 <= token_type < len(symbolic_names):
        raw = symbolic_names[token_type]
        if raw and raw not in ("<INVALID>", ""):
            return raw

    # EOF
    if token_type == -1:
        return "EOF"

    # Guess from text
    t = text.strip()
    if t in KEYWORDS:
        return "KEYWORD"
    if t in PUNCTUATION:
        return "PUNCT"
    if t == ">>":
        return "PATH_OP"
    if t == "--":
        return "LINK_OP"
    # integer
    try:
        int(t)
        return "INT"
    except ValueError:
        pass
    # IP prefix  e.g. 10.0.0.0/8
    if "/" in t and t.replace(".", "").replace("/", "").isdigit():
        return "IP_PREFIX"
    # looks like an identifier
    if t and (t[0].isalpha() or t[0] == "_"):
        return "IDENT"

    return f"<{token_type}>"


def colour_for(friendly: str, text: str) -> str:
    t = text.strip()
    if t in KEYWORDS or friendly == "KEYWORD":
        return KEYWORD_COLOUR
    if t == ">>" or friendly == "PATH_OP":
        return PATH_COLOUR
    if t in PUNCTUATION or friendly in ("PUNCT", "EOF"):
        return PUNCT_COLOUR
    if friendly in ("INT", "IP_PREFIX", "STRING"):
        return LITERAL_COLOUR
    if "ERROR" in friendly or "INVALID" in friendly:
        return ERROR_COLOUR
    return IDENT_COLOUR


def tokenize_stream(input_stream) -> list:
    """Run the ANTLR lexer and return a list of token dicts."""
    lexer  = RouterLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    symbolic = lexer.symbolicNames
    tokens   = []
    for tok in stream.tokens:
        ttype = tok.type
        fname = friendly_name(ttype, tok.text, symbolic)
        tokens.append({
            "line":    tok.line,
            "col":     tok.column,
            "type":    fname,
            "raw_type": ttype,
            "text":    tok.text,
            "channel": tok.channel,
        })
    return tokens


def print_token_table(tokens: list, show_hidden: bool = False):
    """Pretty-print the token table."""
    visible = [t for t in tokens if t["channel"] == 0] if not show_hidden else tokens

    print(f"\n{BOLD}{'LINE':>5}  {'COL':>4}  {'TOKEN TYPE':<20}  TEXT{RESET}")
    print("─" * 65)

    for t in visible:
        colour       = colour_for(t["type"], t["text"])
        text_display = repr(t["text"]) if t["type"] != "EOF" else "<EOF>"
        print(f"{t['line']:>5}  {t['col']:>4}  "
              f"{colour}{t['type']:<20}{RESET}  {text_display}")

    print("─" * 65)
    print(f"{BOLD}Total tokens: {len(visible)} (visible){RESET}")
    hidden_count = len(tokens) - len(visible)
    if hidden_count:
        print(f"{GREY}Hidden (whitespace/comments): {hidden_count}{RESET}")


def print_summary(tokens: list):
    """Print a frequency summary of token types."""
    from collections import Counter
    visible = [t for t in tokens if t["channel"] == 0]
    counts  = Counter(t["type"] for t in visible)

    print(f"\n{BOLD}── Token Type Summary {'─'*30}{RESET}")
    print(f"  {'TOKEN TYPE':<22} {'COUNT':>6}  FREQUENCY")
    print("  " + "─" * 50)
    total = sum(counts.values())
    for ttype, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        colour  = colour_for(ttype, "")
        bar     = "█" * min(cnt * 30 // max(counts.values(), default=1), 30)
        pct     = cnt / total * 100
        print(f"  {colour}{ttype:<22}{RESET}  {cnt:>4}  {pct:5.1f}%  {GREY}{bar}{RESET}")
    print(f"\n  {BOLD}Total visible tokens: {total}{RESET}")


# ── demo source ───────────────────────────────────────────────────────────────
DEMO_SOURCE = """\
topology {
  roles {
    spine  { count: 2 }
    leaf   { count: 1..8 }
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


def main():
    show_hidden  = "--hidden"  in sys.argv
    show_summary = "--summary" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        path = args[0]
        if not os.path.isfile(path):
            print(f"{RED}Error: file not found: {path}{RESET}")
            sys.exit(1)
        print(f"{BOLD}RouterLang Lexical Analyzer  ▸  {path}{RESET}")
        input_stream = FileStream(path, encoding="utf-8")
    else:
        print(f"{BOLD}RouterLang Lexical Analyzer  ▸  [built-in demo source]{RESET}")
        input_stream = InputStream(DEMO_SOURCE)

    tokens = tokenize_stream(input_stream)
    print_token_table(tokens, show_hidden=show_hidden)

    if show_summary:
        print_summary(tokens)

    print(f"\n{GREY}Tips:{RESET}")
    print(f"{GREY}  --summary   show token-type frequency table{RESET}")
    print(f"{GREY}  --hidden    include whitespace/comment tokens{RESET}\n")


if __name__ == "__main__":
    main()