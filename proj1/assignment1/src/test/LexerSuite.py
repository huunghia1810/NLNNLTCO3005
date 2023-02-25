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
        self.assertTrue(TestLexer.test("123char", "123,char,<EOF>", 102))
        self.assertTrue(TestLexer.test("_lorem", "_lorem,<EOF>", 103))
        self.assertTrue(TestLexer.test("lorem_123", "lorem_123,<EOF>", 103))
        self.assertTrue(TestLexer.test("~lorem", "Error Token ~", 104))
        self.assertTrue(TestLexer.test("lorem~", "lorem,Error Token ~", 105))

        self.assertTrue(TestLexer.test("_123", "_123,<EOF>", 106))
        self.assertTrue(TestLexer.test("_1_2_3_4_5", "_1_2_3_4_5,<EOF>", 107))
        self.assertTrue(TestLexer.test("___123456789", "___123456789,<EOF>", 108))
        self.assertTrue(TestLexer.test("_abc~defg", "_abc,Error Token ~", 109))
        self.assertTrue(TestLexer.test("abcd_ef12", "abcd_ef12,<EOF>", 110))

    def test_INTLIT(self):
        self.assertTrue(TestLexer.test("12345", "12345,<EOF>", 111))
        self.assertTrue(TestLexer.test("1__23456", "1,__23456,<EOF>", 112))
        self.assertTrue(TestLexer.test("1_2_3_4_5", "12345,<EOF>", 113))
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 114))
        self.assertTrue(TestLexer.test("00_123_456", "0,0,_123_456,<EOF>", 115))
        self.assertTrue(TestLexer.test("123_", "123,_,<EOF>", 116))
        self.assertTrue(TestLexer.test("0123", "0,123,<EOF>", 117))
        self.assertTrue(TestLexer.test("1 2 3 4 5 6", "1,2,3,4,5,6,<EOF>", 118))
        self.assertTrue(TestLexer.test("-12345", "-,12345,<EOF>", 119))
        self.assertTrue(TestLexer.test("1234 5678", "1234,5678,<EOF>", 120))

    def test_text(self):
        self.assertTrue(TestLexer.test("There are many variations of passages of Lorem Ipsum available"
                                       " Lorem Ipsum is simply dummy text of the printing",
                                       "There,are,many,variations,of,passages,of,Lorem,Ipsum,available"
                                       ",Lorem,Ipsum,is,simply,dummy,text,of,the,printing,<EOF>", 121))
        self.assertTrue(TestLexer.test("namename loop breakk", "namename,loop,breakk,<EOF>", 122))
        self.assertTrue(TestLexer.test("::", "::,<EOF>", 123))
        self.assertTrue(TestLexer.test("*", "*,<EOF>", 136))
        self.assertTrue(TestLexer.test("/", "/,<EOF>", 137))
        self.assertTrue(TestLexer.test("<", "<,<EOF>", 124))
        self.assertTrue(TestLexer.test("!=", "!=,<EOF>", 138))
        self.assertTrue(TestLexer.test("%", "%,<EOF>", 139))
        self.assertTrue(TestLexer.test("!", "!,<EOF>", 140))
        self.assertTrue(TestLexer.test("\\", "Error Token \\", 125))
        self.assertTrue(TestLexer.test("float", "float,<EOF>", 126))
        self.assertTrue(TestLexer.test("\"", "Unclosed String: ", 127))

    def test_operator(self):
        self.assertTrue(TestLexer.test("a + b", "a,+,b,<EOF>", 128))
        self.assertTrue(TestLexer.test(":: == && ++", "::,==,&&,+,+,<EOF>", 129))
        self.assertTrue(TestLexer.test("=ab * cd", "=,ab,*,cd,<EOF>", 130))
        self.assertTrue(TestLexer.test("a - b", "a,-,b,<EOF>", 146))
        self.assertTrue(TestLexer.test("a * b", "a,*,b,<EOF>", 147))
        self.assertTrue(TestLexer.test("a / b", "a,/,b,<EOF>", 148))
        self.assertTrue(TestLexer.test("a + b - c", "a,+,b,-,c,<EOF>", 149))
        self.assertTrue(TestLexer.test("a * b / c", "a,*,b,/,c,<EOF>", 150))

    def test_FLOATLIT(self):
        self.assertTrue(TestLexer.test("1.234 1.2e3 1.E-3", "1.234,1.2e3,1.E-3,<EOF>", 131))
        self.assertTrue(TestLexer.test(".e+15", ".e+15,<EOF>", 132))
        self.assertTrue(TestLexer.test("e-10 .", "e,-,10,.,<EOF>", 133))
        self.assertTrue(TestLexer.test("1_2.3 4E-11", "12.3,4E-11,<EOF>", 134))
        self.assertTrue(TestLexer.test("15e", "15,e,<EOF>", 135))
        self.assertTrue(TestLexer.test("12E", "12,E,<EOF>", 141))
        self.assertTrue(TestLexer.test(".E+15", ".E+15,<EOF>", 142))
        self.assertTrue(TestLexer.test("E-12 .", "E,-,12,.,<EOF>", 143))
        self.assertTrue(TestLexer.test("1_2.3 4e-11", "12.3,4e-11,<EOF>", 145))

    def test_STRINGLIT(self):
        self.assertTrue(TestLexer.test("""\"This is test!\"""",
                                       """This is test!,<EOF>""", 151))
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
                                       """He asked me: \\"Where is John?\\",<EOF>""", 152))
        self.assertTrue(TestLexer.test('"', "Unclosed String: ", 153))
        self.assertTrue(TestLexer.test('""', ",<EOF>", 154))
        self.assertTrue(TestLexer.test('"""', ",Unclosed String: ", 155))
        self.assertTrue(TestLexer.test('"Forget closing string ', "Unclosed String: Forget closing string ", 26))
        self.assertTrue(TestLexer.test('"abc\t"', "abc\t,<EOF>", 156))
        self.assertTrue(TestLexer.test('"abc\n"', "abc\n,<EOF>", 157))
        self.assertTrue(TestLexer.test('"abc\f"', "abc\f,<EOF>", 158))
        self.assertTrue(TestLexer.test('"abc\b"', "abc\b,<EOF>", 163))
        self.assertTrue(TestLexer.test('"abc\'"', "abc\',<EOF>", 164))
        self.assertTrue(TestLexer.test('"abc\n\t\f\b"', "abc\n\t\f\b,<EOF>", 165))
        self.assertTrue(TestLexer.test('"aaa" "bbb"', "aaa,bbb,<EOF>", 159))
        self.assertTrue(TestLexer.test('"abc"""', "abc,,<EOF>", 160))
        self.assertTrue(TestLexer.test('"abc\\""', "abc\\\",<EOF>", 161))
        self.assertTrue(TestLexer.test('"abc\n\n\n\t\f\b"', "abc\n\n\n\t\f\b,<EOF>", 162))

