"""
Jacob Rammer
Sweep mini project
"""


def all_same(l: list) -> bool:
    """Check to see if all elements in a list are the same"""

    if len(l) != 1:
        for i in l:
            if i == l[0]:
                pass
            else:
                return False
    return True


def dedup(l: list) -> list:
    """TODO"""

    index = 0
    deduped_index = 0
    deduped_list = []

    if len(l) != 0:
        deduped_list.append(l[0])

        for i in l:
            if l[index] == deduped_list[deduped_index]:
                pass
            else:
                deduped_list.append(l[index])
                deduped_index += 1
            index += 1

    return deduped_list


def max_run(l: list) -> int:
    """Return the number of the longest consecutive character occurrence in a list"""

    longest = 0
    l_copy = l.copy()
    l_copy.sort()
    max_list = [] #

    if len(l) != 0:
        for i in l_copy:
            if len(l_copy) <= longest and longest == 0:
                longest = 1
                break
            max_list.append(l_copy[0])
            l_copy.pop(l[0])
            while max_list[0] in l_copy:
                max_list.append(l_copy[0])
                l_copy.pop(0)
            if len(max_list) > longest:
                longest = len(max_list)
                max_list.clear()

    return longest
