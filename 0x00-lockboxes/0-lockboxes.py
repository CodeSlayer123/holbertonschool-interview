#!/usr/bin/python3


def canUnlockAll(boxes):
    keys = []
    opened = 0
    for value in boxes[0]:
        keys.append(value)
        opened+=1
    
    for i in range(1, len(boxes)):
        if i in keys:
            opened+=1
            for value in boxes[i]:
                if value not in keys:
                    keys.append(value)
    for i in range(1, len(boxes)):
        if i in keys:
            for value in boxes[i]:
                if value not in keys:
                    keys.append(value)
    for i in range(1, len(boxes)):
        if i in keys:
            for value in boxes[i]:
                if value not in keys:
                    keys.append(value)

    if opened == len(boxes):
        return True
    else:
        return False
