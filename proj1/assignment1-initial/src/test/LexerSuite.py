import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        # self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 101))
