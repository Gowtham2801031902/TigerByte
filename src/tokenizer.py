from collections import namedtuple
import re

# Define Token structure
Token = namedtuple("Token", ["TYPE", "VALUE"])

# Keywords supported in TigerByte
KEYWORDS = {"print"}

# Regex patterns for token types
TOKEN_SPECIFICATION = [
    ("NUMBER",   r"\d+(\.\d+)?"),  # Integer or decimal number
    ("IDENT",    r"[A-Za-z_]\w*"), # Identifiers
    ("OP",       r"[+\-*/=]"),     # Operators (simple)
    ("STRING",   r'"[^"]*"'),      # String literals
    ("SKIP",     r"[ \t]+"),       # Skip spaces and tabs
    ("MISMATCH", r"."),            # Any other character
]

# Compile regex
TOK_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPECIFICATION)
get_token = re.compile(TOK_REGEX).match

def tokenize(code):
    """Tokenizes TigerByte source code into a list of Tokens"""
    pos = 0
    tokens = []
    while pos < len(code):
        match = get_token(code, pos)
        if not match:
            raise SyntaxError(f"Unexpected character: {code[pos]}")

        kind = match.lastgroup
        value = match.group(kind)

        if kind == "NUMBER":
            tokens.append(Token("NUMBER", value))
        elif kind == "IDENT":
            if value in KEYWORDS:
                tokens.append(Token("KEYWORD", value))
            else:
                tokens.append(Token("IDENTIFIER", value))
        elif kind == "OP":
            tokens.append(Token("OPERATOR", value))
        elif kind == "STRING":
            tokens.append(Token("STRING", value))
        elif kind == "SKIP":
            pass  # Ignore spaces
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character: {value}")

        pos = match.end()
    return tokens

# Quick manual test
if __name__ == "__main__":
    example_code = 'print 42 "Hello, TigerByte!" x = 10'
    for token in tokenize(example_code):
        print(token)
