import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 101))

    # def test_2(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 101))

    def test_3(self):
    #     """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
                                       "He asked me: \"Where is John?\",<EOF>", 101))
