import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 101))
        #self.assertTrue(TestLexer.test("1234_567", "1234567,<EOF>", 102))
        #self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 103))
        #self.assertTrue(TestLexer.test(""" "He asked me: \\"where is John?\\"" """, """ He asked me: \\"where is John?\\",<EOF>""", 104))
        #self.assertTrue(TestLexer.test("""a, b, c: integer = 3, 4, 6; """, "succesfull", 105))

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("val_1", "val_1,<EOF>", 1))  # norm
        self.assertTrue(TestLexer.test("_val", "_val,<EOF>", 2))  # with '_' upfront
        self.assertTrue(TestLexer.test("~val", "Error Token ~", 3))  # illegal char upfront
        self.assertTrue(TestLexer.test("1val", "1,val,<EOF>", 4))  # illegal digit upfront
        self.assertTrue(TestLexer.test("val~", "val,Error Token ~", 5))  # illegal char within

        self.assertTrue(TestLexer.test("_123", "_123,<EOF>", 36))
        self.assertTrue(TestLexer.test("_a~b", "_a,Error Token ~", 37))
        self.assertTrue(TestLexer.test("a_b12", "a_b12,<EOF>", 38))
        self.assertTrue(TestLexer.test("_1_2_3", "_1_2_3,<EOF>", 39))
        self.assertTrue(TestLexer.test("___123", "___123,<EOF>", 40))

    def test_integerL(self):
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 6))  # norm
        self.assertTrue(TestLexer.test("1_2_3", "123,<EOF>", 7))  # one '_' between digits
        self.assertTrue(TestLexer.test("1__23", "1,__23,<EOF>", 8))  # many '_' between digits
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 9))  # only 0
        self.assertTrue(TestLexer.test("00_0_0", "0,0,_0_0,<EOF>", 10))  # precede 0

        self.assertTrue(TestLexer.test("0123", "0,123,<EOF>", 41))
        self.assertTrue(TestLexer.test("1000 2000", "1000,2000,<EOF>", 42))
        self.assertTrue(TestLexer.test("123_", "123,_,<EOF>", 43))
        self.assertTrue(TestLexer.test("1 2 3 4 5", "1,2,3,4,5,<EOF>", 44))
        self.assertTrue(TestLexer.test("-1", "-,1,<EOF>", 45))

    def test_keyword(self):
        self.assertTrue(TestLexer.test("auto break boolean do else false float for function if integer return string"
                                       " true while void out continue of inherit array",
                                       "auto,break,boolean,do,else,false,float,for,function,if,integer,return,string"
                                       ",true,while,void,out,continue,of,inherit,array,<EOF>", 11))  # reserves words
        self.assertTrue(TestLexer.test("autoname iff", "autoname,iff,<EOF>", 12))  # only catch kw if stand alone
        
        self.assertTrue(TestLexer.test("+", "+,<EOF>", 46))
        self.assertTrue(TestLexer.test(";", ";,<EOF>", 47))
        self.assertTrue(TestLexer.test("\\", "Error Token \\", 48))
        self.assertTrue(TestLexer.test("main", "main,<EOF>", 49))
        self.assertTrue(TestLexer.test("\"", "Unclosed String: ", 50))

    def test_operator(self):
        self.assertTrue(TestLexer.test("a + b / c", "a,+,b,/,c,<EOF>", 13))  # norm
        self.assertTrue(TestLexer.test("== = ++", "==,=,+,+,<EOF>", 14))  # weird words
        self.assertTrue(TestLexer.test("=a", "=,a,<EOF>", 15)) # catch as norm

    def test_floatL(self):
        self.assertTrue(TestLexer.test("1.234 1.2e3", "1.234,1.2e3,<EOF>", 16))  # norm 1
        self.assertTrue(TestLexer.test("1_234.567 7E-10", "1234.567,7E-10,<EOF>", 17))  # norm 2
        self.assertTrue(TestLexer.test(".e+10", ".e+10,<EOF>", 18))  # missing integerP
        self.assertTrue(TestLexer.test("e-10 .", "e,-,10,.,<EOF>", 19))  # missing both integerP & DecimalP or just dot
        self.assertTrue(TestLexer.test("10e", "10,e,<EOF>", 20))  # missing finalized digits sequence after exp

    def test_stringL(self):
        self.assertTrue(TestLexer.test("""\"I am study PPL!\"""",
                                       """I am study PPL!,<EOF>""", 21))
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
                                       """He asked me: \\"Where is John?\\",<EOF>""", 22))
        self.assertTrue(TestLexer.test('"', "Unclosed String: ", 23))  # single "
        self.assertTrue(TestLexer.test('""', ",<EOF>", 24))  # double "
        self.assertTrue(TestLexer.test('"""', ",Unclosed String: ", 25))  # triple "
        self.assertTrue(TestLexer.test('"Forget closing string ', "Unclosed String: Forget closing string ", 26)) 
        self.assertTrue(TestLexer.test('"abc\t"', "abc\t,<EOF>", 27))
        self.assertTrue(TestLexer.test('"abc\n"', "abc\n,<EOF>", 28))
        self.assertTrue(TestLexer.test('"abc" "def"', "abc,def,<EOF>", 29))
        self.assertTrue(TestLexer.test('"abc"""', "abc,,<EOF>", 30))
        self.assertTrue(TestLexer.test('"abc\\""', "abc\\\",<EOF>", 31))
        self.assertTrue(TestLexer.test('"abc\n\n\n\t\f\b"', "abc\n\n\n\t\f\b,<EOF>", 32))
        #self.assertTrue(TestLexer.test('"\r"', "\r,<EOF>", 33))
        #self.assertTrue(TestLexer.test('"abc\\"', "abc\n,<EOF>", 29))


    def test_some(self):
        self.assertTrue(TestLexer.test("1.2e3", "1.2e3,<EOF>", 104))

