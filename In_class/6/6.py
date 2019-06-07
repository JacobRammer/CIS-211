"""
Jacob Rammer

"""


class Spillage(Exception):
    pass


class Bucket(object):
    """You can put stuff in! You can pour stuff out!"""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        # Initially the bucket is empty
        self.holding = 0

    def pour_in(self, amount: int) -> None:
        """Pour amount of liquid into the bucket,
        if there is enough room left.
        """
        space = self.capacity - self.holding
        if amount > space:
            raise Spillage("Too much! Overflowing!")
        self.holding += amount

    def pour_out(self, requested_amount: int) -> int:
        """Pour UP TO amount of liquid from the
        bucket. If more is requested than the bucket
        currently holds, pour out just what the bucket
        currently holds. Returns the amount of liquid
        actually poured out. See tests below for
        examples.
        """

        return_amount = 0

        if requested_amount > self.holding:
            return_amount = self.holding
            self.holding = 0
            return return_amount
        else:
            self.holding -= requested_amount
            return requested_amount


# b = Bucket(20)
# b.pour_in(10)
# out = b.pour_out(7)
# assert out == 7
# out = b.pour_out(7)
# assert out == 3
# out = b.pour_out(7)
# assert out == 0


"""
selectors
"""


class Selector:
    """
    Abstract base class
    """

    def select(self, l: list):
        raise NotImplementedError("Forgot select method")


class DefaultSelector(Selector):
    def select(self, l: list):
        return l[0]


class Selectable(list):
    """
    Like lists, except we can select from them
    """

    def __int__(self):
        self.selector = DefaultSelector()

    def select(self):
        return self.selector(self)

    def set_selector(self, selector: Selector):
        self.selector = selector


class SelectMax(Selector):

    def select(self, l: list):
        return max(l)


#
# s = Selectable([1, 7, 42, -4, 3, 8])
# print(f"With default selector: {s.select()}")
# s.set_selector(SelectMax)

"""
Tree walking
"""
from typing import List


class Graphic:

    def render(self, tr: "Point") -> List["Point"]:
        raise NotImplementedError("Render not implemented")


class Point(Graphic):

    def __int__(self, x, y):
        self.x = x
        self.y = y

    def render(self, tr: "Point"):
        return [self.x + tr.x, self.y + tr.y]

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Region(Graphic):

    def __int__(self, tr_x: int, tr_y: int):
        self.tr = Point(tr_x, tr_y)
        self.parts = []

    def append(self, part: Graphic):
        self.parts.append(part)

    def render(self, tr: "Point") -> List["Point"]:
        transform = self.tr + tr
        result = []

        for part in self.parts:
            result += part.render(transform)

        return result


scene = Region(5, 5)
a = Region(3, 4)
scene.append(a)
b = Region(2,2)
scene.append(b)
a.apend(Point(6, 2))
a.append(Point(3, 4))
b.append(Point(7, 7))

print(scene.render(0, 0))
