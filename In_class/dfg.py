# # class Tree(object):
# #     """Abstract base class"""
# #
# #     def max_leaf(self) -> int:
# #         raise NotImplementedError("max_leaf must be overridden")
# #
# #
# # class Leaf(Tree):
# #     """Leaves of tree hold positive integers"""
# #
# #     def __init__(self, val: int) -> None:
# #         assert val > 0
# #         self.val = val
# #
# #     def max_leaf(self) -> int:
# #         """You needed to write this basis case"""
# #         return self.val
# #
# #     def __repr__(self):
# #         return f"Leaf {self.val}"
# #
# #
# # class Interior(Tree):
# #     """Interior node has two subtrees"""
# #
# #     def __init__(self, left: Tree, right: Tree) -> None:
# #         self.left = left
# #         # print(self.left)
# #         self.right = right
# #
# #     def max_leaf(self) -> int:
# #         """You needed to write this recursive case,
# #         or something equivalent in function.
# #         """
# #         return max(self.left.max_leaf(), self.right.max_leaf())
# #
# #     def __repr__(self):
# #         return f"Interior: Left: {self.left}, Right: {self.right}"
# #
# #
# # t = Interior(Leaf(4), Interior(Leaf(5), Leaf(3)))
# # assert t.max_leaf() == 5
# from typing import List
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
# # corner = Point(10, 10)
# # small_rect = Rect(corner, 10, 10)
# # larger_rect = Rect(corner, 20, 20)
# # # larger_rect.move(20, 20)
# # print("Smaller rect is {}".format(small_rect))
# # print("Larger rect is {}".format(larger_rect))
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


class CourseRecord:
    def __init__(self, title: str, group: str, grade: int):
        self.title = title
        self.group = group
        self.grade = grade

    def __str__(self):
        return f"{self.title} ({self.group}): {self.grade}"


class Selector:
    def select(self, item: CourseRecord) -> bool:
        raise NotImplementedError("Concrete selector needs 'select' method")


class Transcript(list):
    def select(self, selector: Selector):
        result = []
        for item in self:
            if selector.select(item):
                result.append(item)
        return result


class SelectByGroup(Selector):
    def __init__(self, group: str):
        self.group = group

    def select(self, item: CourseRecord) -> bool:
        return item.group == self.group


my_grades = Transcript()
my_grades.append(CourseRecord("Ancient Greek Cinema", "AL", 3))
my_grades.append(CourseRecord("History of Pasta", "SS", 4))
my_grades.append(CourseRecord("Folk Songs of Austria and Australia", "AL", 2))
for course in my_grades.select(SelectByGroup("AL")):
    print(course)

from typing import List


class Tile:
    def __init__(self, value: int):
        self.value = value


class Matrix:
    def __init__(self, elements: List[List[Tile]]):
        self.tiles = elements
        self.columns = self.group_by_columns()

    def group_by_columns(self):
        cols = []
        for col_i in range(len(self.tiles[0])):
            group = []
            for row_i in range(len(self.tiles)):
                group.append(self.tiles[row_i][col_i])
            cols.append(group)
        return cols

    def magnify_columns(self):
        for col_i in range(len(self.columns)):
            col = self.columns[col_i]
            for tile in col:
                tile.value = tile.value * col_i

    def pr(self):
        for row in self.tiles:
            for tile in row:
                print(f"{tile.value} ", end="")
            print()


m = Matrix([[Tile(1), Tile(1), Tile(1), Tile(1)],
            [Tile(1), Tile(1), Tile(1), Tile(1)],
            [Tile(1), Tile(1), Tile(1), Tile(1)],
            ])
m.magnify_columns()
m.pr()


class Listener:
    def notify(self, event_name: str):
        raise NotImplementedError("Listener subclass needs notify method")


class Door:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, ev: str):
        for listener in self.listeners:
            listener.notify(ev)

    def open(self):
        print("Door opening")
        self.notify_all("open")

    def close(self):
        print("Door closing")
        self.notify_all("close")


class Spy(Listener):
    def __init__(self):
        self.open_count = 0

    def notify(self, event_name: str):
        if event_name == "open":
            self.open_count += 1


monitor = Spy()
front_door = Door()
front_door.open()
front_door.close()
front_door.add_listener(monitor)
front_door.open()
front_door.close()
print(f"Opened {monitor.open_count} times")

from typing import Tuple, List


class Pt:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Pt({self.x}, {self.y})"

    def __ge__(self, other: "Pt") -> bool:
        return self.x >= other.x and self.y >= other.y


class Rect:
    def __init__(self, ll: Pt, ur: Pt):
        assert ur >= ll, "ur must be upper right corner"
        self.ll = ll
        self.ur = ur

    def contains(self, pt: Pt) -> bool:
        return pt >= self.ll and self.ur >= pt

    def __repr__(self):
        return f"{self.ll}, {self.ur}"


class PointCloud(list):
    def region_cloud(self, rect: Rect) -> "PointCloud":

        """Returns PointCloud with points contained in rect"""

        l = []
        for i in self:
            if rect.contains(i):
                l.append(i)

        return l


pc = PointCloud()
pc.append(Pt(1, 1))
pc.append(Pt(3, 3))
pc.append(Pt(4, 4))
pc.append(Pt(8, 8))
selected = pc.region_cloud(Rect(Pt(2, 2), Pt(5, 5)))
print(selected)
# Expecting: [Pt(3,3), Pt(4,4)]

