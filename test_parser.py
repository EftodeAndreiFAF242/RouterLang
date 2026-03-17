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

# --- TEST 5: Valid BGP with explicit peer list ---
valid3 = """
topology { roles { r1 { count: 1 } r2 { count: 1 } } links { r1 -- r2 } }
routing {
  bgp {
    asn { r1: 65001 r2: 65002 }
    neighbors {
      external-peer: 203.0.113.1
    }
  }
}
policy { define P { permit { match any } } }
intent { I1: route t { primary: r1 >> r2 } }
"""
parse(valid3, "valid explicit peer list — should be accepted")

# --- TEST 6: Valid prefix match ---
valid4 = """
topology { roles { r1 { count: 1 } r2 { count: 1 } } links { r1 -- r2 } }
routing { bgp { asn { r1: 65001 r2: 65002 } neighbors: auto } }
policy {
  define P {
    rank 10: permit {
      match prefix 192.0.2.0/24 le 32
      set local-pref 200
    }
  }
}
intent { I1: route t { primary: r1 >> r2 } }
"""
parse(valid4, "valid prefix match and local-pref — should be accepted")

# --- TEST 7: Valid multi-hop path with backup ---
valid5 = """
topology {
  roles { r1 { count: 1 } r2 { count: 1 } r3 { count: 1 } }
  links { r1 -- r2  r2 -- r3 }
}
routing { bgp { asn { r1: 65001 r2: 65002 r3: 65003 } neighbors: auto } }
policy { define P { permit { match any } } }
intent {
  I1: route t {
    primary: r1 >> r2 >> r3
    backup: r1 >> r3
  }
}
"""
parse(valid5, "valid multi-hop path with backup — should be accepted")

# --- TEST 8: Deny action ---
valid6 = """
topology { roles { r1 { count: 1 } r2 { count: 1 } } links { r1 -- r2 } }
routing { bgp { asn { r1: 65001 r2: 65002 } neighbors: auto } }
policy {
  define P {
    rank 10: deny {
      match prefix 10.0.0.0/8 le 32
    }
    rank 20: permit {
      match any
    }
  }
}
intent { I1: route t { primary: r1 >> r2 } }
"""
parse(valid6, "valid deny then permit policy — should be accepted")