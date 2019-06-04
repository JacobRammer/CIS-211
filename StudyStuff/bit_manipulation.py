"""
Jacob Rammer

"""

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

#  W 2019 number 3 from final


