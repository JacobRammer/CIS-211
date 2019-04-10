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

    longest_run = 0
    l_copy = l.copy()  # don't change original list
    max_list = []

    if len(l) == 0 or len(l) == 1:
        return len(l)
    for i in l_copy:
        max_list.append(l_copy[0])
        l_copy.pop(0)
        while len(l_copy) >= 1 and max_list[0] == l_copy[0]:
            max_list.append(l_copy[0])
            l_copy.pop(0)
        if len(max_list) >= longest_run:
            longest_run = len(max_list)
            max_list.clear()

    return longest_run
