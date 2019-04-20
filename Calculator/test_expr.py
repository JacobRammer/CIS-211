"""Unit tests for expr.py"""

import unittest
from expr import *


class TestIntConst(unittest.TestCase):

    def test_eval(self):
        five = IntConst(5)
        self.assertEqual(five.eval(), IntConst(5))

    def test_str(self):
        twelve = IntConst(12)
        self.assertEqual(str(twelve), "12")

    def test_repr(self):
        forty_two = IntConst(42)
        self.assertEqual(repr(forty_two), f"IntConst(42)")


class TestPlus(unittest.TestCase):

        def test_plus_str(self):
            exp = Plus(IntConst(5), IntConst(4))
            self.assertEqual(str(exp), "(5 + 4)")

        def test_nested_str(self):
            exp = Plus(Plus(IntConst(4), IntConst(5)), IntConst(3))
            self.assertEqual(str(exp), "((4 + 5) + 3)")

        def test_repr_simple(self):
            exp = Plus(IntConst(12), IntConst(13))
            self.assertEqual(repr(exp), "Plus(IntConst(12), IntConst(13))")

        def test_repr_nested(self):
            exp = Plus(IntConst(7), Plus(IntConst(4), IntConst(2)))
            self.assertEqual(repr(exp), "Plus(IntConst(7), Plus(IntConst(4), IntConst(2)))")

        def test_addition_simple(self):
            exp = Plus(IntConst(4), IntConst(8))
            self.assertEqual(exp.eval(), IntConst(12))

        def test_additional_nested(self):
            exp = Plus(IntConst(7), Plus(IntConst(2), IntConst(3)))
            self.assertEqual(exp.eval(), IntConst(12))

if __name__ == "__main__":
    unittest.main()
