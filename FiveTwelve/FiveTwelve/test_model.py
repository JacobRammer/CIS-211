"""
Tests for model.py.

Note that the unittest module predates PEP-8 guidelines, which
is why we have a bunch of names that don't comply with the
standard.
"""
import model
from model import Vec, Board
import unittest
import sys


class TestVec(unittest.TestCase):

    def test_equality(self):
        v1 = Vec(7, 12)
        v2 = Vec(8, 13)
        self.assertNotEqual(v1, v2)
        v3 = Vec(7, 12)
        self.assertEqual(v1, v3)

    def test_addition(self):
        v1 = Vec(8, 7)
        v2 = Vec(12, 15)
        # print(Vec.__add__(v1, v2))
        self.assertEqual(v1 + v2, Vec(20, 22))
        # Addition does not modify the points that have been added
        self.assertEqual(v1, Vec(8, 7))
        self.assertEqual(v2, Vec(12, 15))

class TestBoardConstructor(unittest.TestCase):

    def test_default(self):
        board = Board()
        self.assertEqual(board.tiles, [[None, None, None, None],
                                       [None, None, None, None],
                                       [None, None, None, None],
                                       [None, None, None, None]])

    def test_3x5(self):
        board = Board(rows=3, cols=5)
        self.assertEqual(board.tiles, [[None, None, None, None, None],
                                 [None, None, None, None, None],
                                 [None, None, None, None, None]])


if __name__ == "__main__":
    unittest.main()
