#!/usr/bin/python3
"""
0_rain
"""
def rain(walls):
    total = 0
    print(walls)
    for i in walls:
        if i == 0:
            print(i, "yes")
            walls.remove(i)
        else:
            print(i, "no")
    
    for i in walls:
        if i == 0:
            print(i, "yes")
            walls.remove(i)
        else:
            print(i, "no")
    print(walls)
    size = len(walls)
    last = walls[size - 1]
    for j in walls:
        if j != last:
            total += j
    print(total)
    return total
