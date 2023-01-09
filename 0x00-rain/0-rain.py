#!/usr/bin/python3
"""
0_rain
"""
def rain(walls):
    
    if len(walls) <= 0:
        return 0
    total = 0
    print(walls)
    for i in walls:
        if i == 0:
            walls.remove(i)
    for i in walls:
        if i == 0:
            walls.remove(i)

    size = len(walls)
    for j in range(size - 1):
        total += walls[j]
    return total
