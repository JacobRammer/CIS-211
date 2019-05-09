"""
Jacob Rammer

"""
from typing import Tuple
from enum import Enum


def pack(a: int, b: int, c: int) -> int:
    word = (a & 3) << 6 | (b & 7) << 3 | (c & 7)
    return word


def unpack(w: int) -> Tuple[int, int, int]:
    c = w & 7
    a = (w >> 6) & 3
    b = (w >> 3) & 7

    return a, b, c


# a, b, c, = 2, 5, 1
# w = pack(a, b, c,)
# x, y, z = unpack(w)
# print(f"X: {x}, Y: {y}, Z: {z}")

class Direction(Enum):
    North = 0
    NorthEast = 1
    East = 2
    SouthEast = 3
    South = 4
    SouthWest = 5
    West = 6
    NorthWest = 7


def encode(dir: Direction, steps: int) -> int:
    assert steps <= 31

    w = 0
    w = w | (dir.value << 5)
    w = w | steps

    return w


def decode(w: int) -> Tuple[Direction, int]:
    dir_i = (w >> 5) & 7  # 7 for 3 bit field (2^0, 2^1, 2^2)
    steps = w & 31  # 5 1 bits
    dir = Direction(dir_i)

    return dir, steps


# w = encode(Direction.NorthWest, 17)
# dir, steps = decode(w)
# print(f"{steps}, {dir}")

def count_1_bits(w: int) -> int:
    """
    W is a positive number, result is the number
    of 1 bits in w.
    Example: (0b101101) == 4
    """

    count = 0

    for i in bin(w):
        if i == "1":
            count += 1

    return count


print(count_1_bits(45))
