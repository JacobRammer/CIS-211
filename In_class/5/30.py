"""
Jacob Rammer

"""


# digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
#           "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13,
#           "E": 14, "F": 15}
#
#
# def hex_str_to_int(s: str) -> int:
#     """
#     Example: hex_str_to_int("ff") == 255
#     """
#
#     sum = 0
#     multiplier = 1
#     s = s.upper()
#     for i in s[::-1]:
#         sum += digits[i] * multiplier
#         multiplier *= 16
#
#     return sum
#
#
# def hex_str_to_int_v2(s: str) -> int:  # wrong, check posted code
#     """
#     Example: hex_str_to_int("ff") == 255
#     """
#
#     sum = 0
#     s = s.upper()
#     for i in s:
#         sum += 16 * sum + digits[i]
#
#     return sum
#
#
# def hex_str_to_int_v3(s: str) -> int:
#     """
#     Example: hex_str_to_int("ff") == 255
#     """
#
#     sum = 0
#     s = s.upper()
#     for i in s[::-1]:
#         sum = (sum << 4) | digits[i]
#
#     return sum
#
#
# print(hex_str_to_int_v3("ff"))

class Tree:
    """Abstract base class"""

    def select(self, f) -> str:
        """f is function from string to bool;
        returns concatenation of substrings
        for which f(t) is true.
        """
        raise NotImplementedError("huh?")


class Leaf(Tree):
    def __init__(self, t: str):
        self.text = t

    def select(self, f) -> str:
        if f(self.text):
            return self.text
        return ""


class Inner(Tree):
    def __init__(self):
        self.parts = []

    def append(self, t: str):
        self.parts.append(t)

    def select(self, f) -> str:
        # result = ""
        # for part in self.parts:
        #    result += part.select(f)
        # return result
        return "".join([p.select(f) for p in self.parts])


t = Inner()
s = Inner()
s.append(Leaf("foo"))
s.append(Leaf("river"))
t.append(s)
t.append(Leaf("foobaz"))

result = t.select(lambda x: len(x) <= 5)
print(result)  # expect "fooriver"
"""
All columns have the same sum
"""


def all_col_same_sum(matrix):
    sum = 0
    if len(matrix) == 0:
        return True  # because math

    sample = col_sum(matrix, 0)
    for col_i in range(len(matrix[0])):
        if sample != col_sum(matrix, col_i):
            return False
    return True


def col_sum(matrix, col_i: int) -> int:
    sum = 0

    for i in matrix:
        sum += i[col_i]

    return sum


m = [[0, 1, 2],
     [2, 1, 0],
     [3, 3, 3]]

print(all_col_same_sum(m))
