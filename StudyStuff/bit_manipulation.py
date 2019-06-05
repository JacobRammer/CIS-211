"""
Jacob Rammer

"""
from typing import Tuple
from enum import Enum

"""
Observation
1 << 0: 01
1 << 1: 0001 -> 00010
1 << 2: 0001 -> 000100

Example: is the 2nd bit set?
6:  110 
    100 &
    ---
    100
"""


def nth_bit_set(x: int, nth: int):
    print(1 << nth)
    if x & (1 << nth):
        return True
    return False


"""
0b110&
0b100)
"""
# print(nth_bit_set(6, 2))  # 6:0b110, checking against 100

"""
Example: set the 0th bit of the binary representation of 6
6:          110
1 << 1      010 |
            ---
            110 
"""


def set_nth_bit(x: int, n: int):
    n = n - 1
    print(bin(1 << n))
    print(bin(20))
    print(bin(x | 1 << n))
    return x | 1 << n


# print(set_nth_bit(20, 2))

"""
Many early personal computers including the TRS-80 and Kaypro II used the
Zilog Z80 8-bit microprocessor. The 8-bit instruction code for a Z80 is divided into three
parts:
• x: a 2-bit field (bits 6..7)
• y: a 3-bit field (bits 3..5)
• z: a 3-bit field (bits 0..2)
In the program below I have provided a function “pack” for packing fields x, y, and z into
an integer. Complete the corresponding function “unpack” for extracting the x, y, and z
fields, such that unpack(pack(x, y, z)) = x, y, z provided 0 ≤ x ≤ 3, 0 ≤ y ≤ 7, 0 ≤ z ≤ 7.

"""


def pack(a: int, b: int, c: int) -> int:
    word = (a & 3) << 6 | (b & 7) << 3 | (c & 7)
    return word


def unpack(word: int) -> Tuple[int, int, int]:
    c = word & 7
    b = (word >> 3) & 7
    a = (word >> 6) & 3

    return a, b, c


w1 = pack(3, 7, 7)
print(unpack(w1))
assert unpack(w1) == (3, 7, 7)

w2 = pack(1, 1, 1)
print(unpack(w2))
assert unpack(w2) == (1, 1, 1)

"""
Determine the longest number of 1 bits in a word
"""


def longest_1_run(word: int) -> int:
    """
    What is the longest run of 1 bits in the
    (positive or unsigned) integer?  For example,
    longest_1_run(0b011101101100) == 3
    longest_1_run(0b000000000000) == 0
    longest_1_run(0b011111011011) == 5
    """

    assert word >= 0

    longest_run = 0
    current_run = 0

    while word != 0:
        if (word & 1) == 1:
            current_run += 1
        else:
            current_run = 0

        word = word >> 1

        if current_run > longest_run:
            longest_run = current_run

    return longest_run


# print(longest_1_run(0b011101101100))
# print(longest_1_run(0b000000000000))
# print(longest_1_run(0b011111011011))

"""
Sometimes we compactly encode a path such as movement of a pen or movement of a monster in a video game as a series of small moves in a grid. In this problem, we
will pack one of 8 compass directions into bits 5..7 of a byte and use the remaining bits 0..4
to record a distance of up to 31 units. Finish the three functions so that they correctly pack
and extract the information. Recall that you can convert a Direction d to an integer as
d.value and you can convert an integer i in the range 0..7 to a Direction as Direction(i).
You may assume that values provided to to_dir and to_dist were produced by encode.
"""


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
    """
    Return 8-bit encoding of movement
    """

    return (dir.value << 5) | (steps & 31)


def to_dir(word: int) -> Direction:
    """
    Extract direction value from encoded movement
    """

    return Direction(word >> 5)


def to_steps(word: int) -> int:
    """
    Extract number of steps from movement
    """
    return word & 31


# east13 = encode(Direction.East, 13)
# print(to_dir(east13))
# print(to_dir(east13))


"""
Bovine Systems is not a real company, and they do not make the CPU chip
BS2018, but if they did it would use an 8-bit (unsigned) instruction code with three fields,
x (bits 5..7), y (bits 1..4), and z (bit zero). Finish the pack function to complement the
unpack function below. Note the examples, which show that it will be necessary to mask
the input values.
"""


def pack_two(x: int, y: int, z: int) -> int:
    """
    Pack x, y, and z into fields of an 8-bit unsigned integer.
    x: bits 5..7 (3 bits)
    y: bits 1..4 (4 bits)
    z: bit
    """

    return (x << 5) | (y << 1) | z


def unpack_two(word: int) -> Tuple[int, int, int]:
    """
    Unpacks unsigned 8-bit int into
    bits 5..7 => x, bits 1..4 => y, bit 0 => z
    Input and all outputs are unsigned.
    """
    x = (word >> 5) & 7
    y = (word >> 1) & 15
    z = word & 1
    return x, y, z


print("(15, 15, 15) => {} (expect (7, 15, 1))".format(unpack_two(pack_two(15, 15, 15))))
print("(3, 3, 3) => {} (expect 3, 3, 1)".format(unpack_two(pack_two(3, 3, 3))))
print("(0, 3, 0) => {} (expect 0, 3, 0)".format(unpack_two(pack_two(0, 3, 0))))
