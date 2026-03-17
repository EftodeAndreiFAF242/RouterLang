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

# --- VALID TEST ---
valid1 = open("tests/valid/minimal_program.rl").read()
parse(valid1, "minimal valid program")

# --- INVALID TEST ---
invalid1 = """
topology { roles { r { count: 1 } } links { r -- r } }
routing { }
policy { define P { permit { match any } } }
intent { I1: route t { primary: r >> r } }
"""
parse(invalid1, "empty routing block — should be rejected")