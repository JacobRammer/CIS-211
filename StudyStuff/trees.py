"""
Jacob Rammer

"""

"""
We will define the depth of a tree to be 1 if it is a leaf, and otherwise 1 more
than the maximum depth of its child subtrees. Complete classes Inner and Leaf so that the
program produces the expected output.

"""


class Tree(object):
    def depth(self) -> int:
        raise NotImplementedError("depth method must be implemented")


class Inner(Tree):
    def __init__(self, left: Tree, right: Tree):
        self.left = left
        self.right = right

    def __repr__(self):
        return "Inner({}, {})".format(self.left, self.right)

    def depth(self):
        t = self.left
        r = self.right.depth()
        return 1 + max(self.left.depth(), self.right.depth())


class Leaf(Tree):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return "Leaf({})".format(self.value)

    def depth(self):
        return 1


skewed = Inner(Leaf(1), Inner(Leaf(2), Leaf(3)))
# print("{} has depth {}".format(skewed, skewed.depth()))

way_skewed = Inner(Leaf(1), Inner(Leaf(2), Inner(Leaf(3), Leaf(4))))
# print("{} has depth {}".format(way_skewed, way_skewed.depth()))

balanced = Inner(Inner(Leaf(1), Leaf(2)), Inner(Leaf(3), Leaf(4)))
# print("{} has depth {}".format(balanced, balanced.depth()))


"""
 Finish the Inner and Leaf classes below so that t.sum_in_range(min, max)
returns the sum of the leaves whose values are between min and max inclusive.
"""


class Tree:
    def sum_in_range(self, min_val: int, max_val: int) -> int:
        """Sum of leaf values in range min_val .. max_val"""
        raise NotImplementedError("Hey! You forgot!")


class Leaf(Tree):
    def __init__(self, v: int):
        self.value = v

    def sum_in_range(self, min_val: int, max_val: int) -> int:
        """Sum of leaf values in range min_val .. max_val"""

        if max_val > self.value > min_val:
            return self.value
        else:
            return 0


class Inner(Tree):
    def __init__(self, left: Tree, right: Tree):
        self.left = left
        self.right = right

    def sum_in_range(self, min_val: int, max_val: int) -> int:
        """Sum of leaf values in range min_val .. max_val"""

        sum = 0
        sum += self.left.sum_in_range(min_val, max_val)
        sum += self.right.sum_in_range(min_val, max_val)

        return sum


t = Inner(Leaf(5), Inner(Inner(Leaf(8), Leaf(3)), Leaf(6)))
print(t.sum_in_range(4, 7))
print(t.sum_in_range(-3, -5))
print(t.sum_in_range(0, 10))
