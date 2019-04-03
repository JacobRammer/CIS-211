"""
# TODO Title
CIS 210 W19 Project #

Author: [Jacob Rammer]

Credits: [N/A]

# TODO Description
"""

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self):
        print(f"{self.x}, {self.y}")

p = Point(1, 2)
# p.move(1, 1)
p.__str__()
# print(p.x, p.y)


