import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from src.parser.RouterLangLexer import RouterLangLexer
from src.parser.RouterLangParser import RouterLangParser

def parse(text, label=""):
    input_stream = InputStream(text)
    lexer = RouterLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RouterLangParser(stream)

    errors = []

    class CollectErrors(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            errors.append(f"Line {line}:{column} — {msg}")

    parser.removeErrorListeners()
    parser.addErrorListener(CollectErrors())

    tree = parser.program()

    if errors:
        print(f"❌ REJECTED — {label}")
        for e in errors:
            print(f"   {e}")
    else:
        print(f"✅ ACCEPTED — {label}")

# --- TEST 1: Valid minimal program ---
valid1 = open("tests/valid/minimal_program.rl").read()
parse(valid1, "minimal valid program")

# --- TEST 2: Empty routing block ---
invalid1 = """
topology { roles { r { count: 1 } } links { r -- r } }
routing { }
policy { define P { permit { match any } } }
intent { I1: route t { primary: r >> r } }
"""
parse(invalid1, "empty routing block — should be rejected")

# --- TEST 3: Single hop path ---
invalid2 = open("tests/invalid/single_hop_path.rl").read()
parse(invalid2, "single hop path — should be rejected")

# --- TEST 4: Valid guard expression ---
valid2 = """
topology { roles { r1 { count: 1 } r2 { count: 1 } } links { r1 -- r2 } }
routing { bgp { asn { r1: 65001 r2: 65002 } neighbors: auto } }
policy {
  define P {
    rank 10: permit {
      match any
      if neighbor.state == DRAINED
    }
  }
}
intent { I1: route t { primary: r1 >> r2 } }
"""
parse(valid2, "valid guard expression — should be accepted")