"""
Jacob Rammer
Waldo mini project
"""
from typing import List

Waldo = "W"
Other = "."


def all_row_exists_waldo(grid: List[List[str]]) -> bool:
    waldo = True
    for row in grid:
        if not waldo:
            break
        if Waldo in row:
            waldo = True
        else:
            waldo = False
    return waldo


def exists_row_all_waldo(grid: List[List[str]]) -> bool:
    for row in grid:
        all_waldos = True
        for col in row:
            if col != Waldo:
                all_waldos = False
                break
        if all_waldos:
            return True
        # if it's all waldos
        # return True
    return False


def all_col_exists_waldo(grid: List[List[str]]) -> bool:
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


def all_row_all_waldo(grid: List[List[str]]) -> bool:
    waldo = True

    for row in grid:
        if Other in row:
            return False
        else:
            waldo = True

    return waldo


def all_col_all_waldo(grid: List[List[str]]) -> bool:
    waldo = True

    for col in grid:
        for row in col:
            if Waldo in row:
                waldo = True
            else:
                return False
    return waldo


def exists_col_all_waldo(grid: List[List[str]]) -> bool:
    if len(grid) == 0:
        return False

    found_waldo = False

    for col_i in range(len(grid[0])):
        for row in grid:
            if row[col_i] == Waldo:
                found_waldo = True
            else:
                found_waldo = False

    return found_waldo


def exists_row_exists_waldo(grid: List[List[str]]) -> bool:
    for row in grid:
        if Waldo in row:
            return True

    return False


def exists_col_exists_waldo(grid: List[List[str]]) -> bool:
    for row in grid:
        for col in row:
            if Waldo in col:
                return True

    return False
