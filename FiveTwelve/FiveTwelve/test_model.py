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

# board = model.Board()
# board.place_tile()
# print(board.tiles)
# board.place_tile()
# print(board.tiles)

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

    def test_constructed_empties(self):
        """A newly constructed Board should always have at least
        one empty space.
        """
        board = model.Board()
        self.assertTrue(board.has_empty())


class TestScaffolding(unittest.TestCase):

    def test_to_from_list(self):
        """to_list and from_list should be inverse"""
        board = model.Board()
        as_list = [[0, 2, 2, 4], [2, 0, 2, 8], [8, 2, 2, 4], [4, 2, 2, 0]]
        board.from_list(as_list)
        self.assertEqual(board.to_list(), as_list)

    def test_from_to(self):
        """to_list and from_list should be inverse"""
        board = model.Board()
        board.place_tile()
        board.place_tile(value=32)
        board.place_tile()
        as_list = board.to_list()
        board.from_list(as_list)
        again = board.to_list()
        self.assertEqual(as_list, again)


if __name__ == "__main__":
    unittest.main()
