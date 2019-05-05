# class Tree(object):
#     """Abstract base class"""
#
#     def max_leaf(self) -> int:
#         raise NotImplementedError("max_leaf must be overridden")
#
#
# class Leaf(Tree):
#     """Leaves of tree hold positive integers"""
#
#     def __init__(self, val: int) -> None:
#         assert val > 0
#         self.val = val
#
#     def max_leaf(self) -> int:
#         """You needed to write this basis case"""
#         return self.val
#
#     def __repr__(self):
#         return f"Leaf {self.val}"
#
#
# class Interior(Tree):
#     """Interior node has two subtrees"""
#
#     def __init__(self, left: Tree, right: Tree) -> None:
#         self.left = left
#         # print(self.left)
#         self.right = right
#
#     def max_leaf(self) -> int:
#         """You needed to write this recursive case,
#         or something equivalent in function.
#         """
#         return max(self.left.max_leaf(), self.right.max_leaf())
#
#     def __repr__(self):
#         return f"Interior: Left: {self.left}, Right: {self.right}"
#
#
# t = Interior(Leaf(4), Interior(Leaf(5), Leaf(3)))
# assert t.max_leaf() == 5
from typing import List


#
#
# class Point(object):
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
#     def move(self, dx: int, dy: int):
#         self.x += dx
#         self.y += dy
#
#     def __str__(self):
#         return "Point({}, {})".format(self.x, self.y)
#
#
# class Rect(object):
#     def __init__(self, ll: Point, width: int, height: int):
#         self.ll = ll
#         self.height = height
#         self.width = width
#
#     def move(self, dx: int, dy: int):
#         self.ll.move(dx, dy)
#
#     def ur(self) -> Point:
#         return Point(self.ll.x + self.width, self.ll.y + self.height)
#
#     def __str__(self):
#         return "Rect({}, {})".format(self.ll, self.ur())
#
#
# corner = Point(10, 10)
# small_rect = Rect(corner, 10, 10)
# larger_rect = Rect(corner, 20, 20)
# larger_rect.move(20, 20)
# print("Smaller rect is {}".format(small_rect))
# print("Larger rect is {}".format(larger_rect))
#
#
# class NumberGrid(object):
#     """A square grid of numbers"""
#
#     def __init__(self, values: List[List[int]]):
#         self.values = values
#         for row in values:
#             assert len(row) == len(values)  # Grid is square
#
#     def is_balanced(self) -> bool:
#
#         """"Balanced if sum of each row and column is equal"""
#         target = 0
#         for item in self.values[0]:
#             target += item
#             # Each row the same
#         for row in self.values:
#             total = 0
#             for item in row:
#                 total += item
#             if total != target:
#                 return False
#                 # Each column the same
#         for col in range(len(self.values)):
#             total = 0
#             for row in range(len(self.values)):
#                 total += self.values[row][col]
#             if total != target:
#                 return False
#
#         return True
#
#
# assert NumberGrid([[2, 7, 6], [9, 5, 1], [4, 3, 8]]).is_balanced()
# assert not (NumberGrid([[2, 7, 6], [9, 7, 1], [4, 3, 8]]).is_balanced())
# print("Passed two simple test cases on 3x3 grid")

def every_column_zero(matrix: List[List[int]]) -> bool:
    """matrix is 4 lists of 4 integers (4 rows of 4 columns each).
    Return True iff each column has at least one element with value 0.
    """
    for col in range(len(matrix)):
        has_zero = False
        for row in matrix:
            test = row[col]
            if row[col] == 0:
                has_zero = True
        if not has_zero:
            return False
    return True


assert every_column_zero([[1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1]])
assert not every_column_zero([[1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 0]])
