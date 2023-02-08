import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # Lexer - question 1
    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("abc a12", "abc,a12,<EOF>", 102))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("abc A12", "abc,Error Token A", 103))

    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    # def test_mixed_id(self):
    #     self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))

    # Lexer - question 2
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("1.0", "1.0,<EOF>", 103))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("1.0e-12", "1.0e-12,<EOF>", 104))

    # Lexer - question 3
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'", "'Yanxi Palace - 2018',<EOF>", 105))