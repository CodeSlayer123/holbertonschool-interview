#!/usr/bin/python3
"""
0_rain
"""

def rain(walls):

    if len(walls) <= 0 or 0 not in walls:
        return 0
    total = 0
    count = 0
    for i in range(len(walls)):
        if walls[i] > 0:
            count = 0
            x = walls[i]
            for j in range(i + 1, len(walls)):
                if walls[j] > 0:
                    y = walls[j]
                    break
                if j == len(walls) - 1:
                    count = 0
                    break
                count += 1

            if x < y:
                total += (count * x)
            else:
                total += (count * y)

    return total
