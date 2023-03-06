#!/usr/bin/python3
"""Islang perimeter algo"""


def island_perimeter(grid):
    """Islang perimeter algo"""

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] == 1):
                if (grid[i][j+1] == 0):
                    total += 1
                if (grid[i][j-1] == 0):
                    total += 1
                if (grid[i-1][j] == 0 ):
                    total += 1
                if (grid[i+1][j] == 0):
                    total += 1
    return total