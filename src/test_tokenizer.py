import unittest
from tokenizer import tokenize, Token

class TestTokenizer(unittest.TestCase):
    def test_basic_print(self):
        code = 'print 42'
        expected = [Token("KEYWORD", "print"), Token("NUMBER", "42")]
        self.assertEqual(tokenize(code), expected)

    def test_identifiers_and_strings(self):
        code = 'print "Hi" my_var = 5'
        expected = [
            Token("KEYWORD", "print"),
            Token("STRING", '"Hi"'),
            Token("IDENTIFIER", "my_var"),
            Token("OPERATOR", "="),
            Token("NUMBER", "5")
        ]
        self.assertEqual(tokenize(code), expected)

if __name__ == "__main__":
    unittest.main()
