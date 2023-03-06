#!/usr/bin/python3

def island_perimeter(grid):
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