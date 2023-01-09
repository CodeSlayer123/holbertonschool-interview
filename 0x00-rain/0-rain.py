#!/usr/bin/python3
"""
0_rain
"""
def rain(walls):
    total = 0
    for i in walls:
        if i == 0:
            walls.remove(i)

    for i in walls:
        if i == 0:
            walls.remove(i)

    size = len(walls)
    last = walls[size - 1]
    for j in walls:
        if j != last:
            total += j
    return total
