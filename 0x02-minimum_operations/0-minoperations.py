#!/usr/bin/python3
"""Computes minimum amount of operations needed to reach n letters of H"""

H = "H"
chars = 1
operations = 0
copied = ""


def minOperations(n):
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
