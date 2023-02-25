import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program(self):
        """Simple program: int main() {} """
        # input = """delta: integer = 3;"""
        # expect = "successful"

        # input = """main: function void () {}"""
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""

#         input = """a, b, c: integer = 4, 6;"""
#         input = """/* A C-style comment */
# a: integer =5; // A C++ style comment"""
#
#         input = """{
# r, s: int;
# r = 2.0;
# a, b: array [5] of int;
# s = r * r * myPI;
# a[0] = s;
# }"""
#         input = """fact: function integer (n: integer) {
#         foo(2 + x, 4.0 / y);
#         goo();
#         }"""

        #expect = "Error on line 1 col 29: ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
