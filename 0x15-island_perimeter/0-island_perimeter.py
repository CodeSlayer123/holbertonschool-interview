#!/usr/bin/python3
"""Islang perimeter algo"""


def island_perimeter(grid):
    """Island perimeter algo"""
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):

                #left
                if (j == len(grid[i]) - 1):
                    total +=1
                elif (grid[i][j+1] == 0):
                    total += 1

                #right
                if (j == 0):
                    total += 1
                elif (grid[i][j-1] == 0):
                    total += 1

                #above
                if (i == 0):
                    total += 1
                elif (grid[i-1][j] == 0 ):
                    total += 1

                #below
                if (i == len(grid) - 1):
                    total += 1
                elif (grid[i+1][j] == 0):
                    total += 1

    return total