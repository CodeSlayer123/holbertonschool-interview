#!/usr/bin/python3
"""Islang perimeter algo"""


def island_perimeter(grid):
    """Island perimeter algo"""
    total = 0
    for i in range(len(grid) - 1):
        for j in range(len(grid[i]) - 1):
            if (grid[i][j] == 1):

                if (j == len(grid[i]) - 1):
                    total +=1
                elif (grid[i][j+1] == 0):
                    total += 1

                if (j == 0):
                    total += 1
                elif (grid[i][j-1] == 0):
                    total += 1

                if (i == len(grid) - 1):
                    total += 1
                elif (grid[i-1][j] == 0 ):
                    total += 1

                if (i == 0):
                    total += 1
                elif (grid[i+1][j] == 0):
                    total += 1

    return total