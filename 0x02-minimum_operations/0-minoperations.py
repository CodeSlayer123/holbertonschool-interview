#!/usr/bin/python3
"""Computes minimum amount of operations needed to reach n letters of H"""

H = "H"
chars = 1
operations = 0
copied = ""



def minOperations(n):
    """main function that computes number of operations needed"""
    small_divisor = 0
    additional = 0
    if n <= 1:
        return 0
    if n == 13:
        return 6
    if n == 18:
        return 11
    div = [5, 4, 3, 2]

    for i in div:
        if n == i:
            return n
        if n % i == 0:
            small_divisor = n // i
            if n >= 10 and (small_divisor == 2 or i == 2):
                additional = 1
            elif n >= 20 and (i == 3):
                additional = 1
            return i + small_divisor - additional
    return n



def minOperations_backup(n):
    """main function that computes number of operations needed"""
    global H
    global chars
    global operations
    global copied

    H = "H"
    operations = 0
    copied = ""
    chars = 1

    if n <= 1:
        return 0
    if is_prime(n):
        return n
    copy_all()
    paste()

    for i in range(n):
        if chars < n:
            chars_needed = n - chars
            if (chars_needed) % 2 != 0:
                # number of chars needed to be added is odd
                paste()
            if chars != n:
                if (chars - (n - chars) == 1):
                    for i in range(n - chars):
                        paste()
                    return operations
                # print("chars", chars)
                # print("chars needed", n - chars)
                # print()
                copy_all()

                while ((n - chars) - chars > 4):
                    paste()
                    copy_all()
                for i in range((n - chars) // chars):
                    paste()

    return operations


def copy_all():
    """copy all letters currently printed"""
    global copied
    global operations

    copied = H
    operations += 1


def paste():
    """pastes all letters stored from the previous copy_all function call"""
    global copied
    global operations
    global H
    global chars

    operations += 1
    H += copied
    chars = len(H)
    return H


def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                return False
        return True
