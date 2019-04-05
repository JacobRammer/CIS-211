"""
CIS 211
Jacob Rammer

Point class mini project
"""


class Point:
    """Point class that has x and y coordinates"""

    def __init__(self, x: int, y: int):
        """Create x and y values"""

        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """Move to (x + dx, y + dy)"""

        self.x += dx
        self.y += dy

    def __eq__(self, other: "Point") -> bool:
        """Checks to see if the coordinate of multiple points are the same"""

        return self.x == other.x and self.y == other.y

    def __str__(self):
        """Print the coordinate of the point"""

        return f"({self.x}, {self.y})"
