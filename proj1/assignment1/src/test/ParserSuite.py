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

        #input = """a, b, c: integer = 3, 4, 6;"""

        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
