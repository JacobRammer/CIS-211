"""
Jacob Rammer

"""
from typing import List

# for all columns, there exists a Waldo
# "there is a Waldo in every column

Waldo = "Waldo"


def all_columns_exists_waldo(grid: List[List[str]]) -> bool:
    # for each column
    # if no waldo in that column
    # found a waldo = false
    # for element in each row of the column
    # if it's a waldo
    # found a waldo = true
    # if not found a waldo:
    # return false
    # return true

    if len(grid) == 0:
        return True

    for col_i in range(len(grid[0])):
        found_waldo = False
        for row_i in range(len(grid)):
            if grid[row_i][col_i] == Waldo:
                found_waldo = True
        if not found_waldo:
            return False

    return True


# Some row is all waldos

def exists_row_all_waldo(grid: List[List[str]]) -> bool:
    for row in grid:  # if it's all waldos, return true
        all_waldos = True
        for col in row:
            if col != Waldo:
                all_waldos = False
                break
        if not all_waldos:
            return True

    return False
