#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))




n = 2
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 5
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 6
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 8
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 10
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 13
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
"""
n = 12
H => Copy All => Paste => HH => Copy All => Paste =>HHHH => Copy All => Paste =>HHHHHHHH => Paste => HHHHHHHHHHHH
Number of operations: 7
"""
"""
n = 5
H => Copy All => Paste => HH => Paste => HHH => Paste => HHHH => Paste => HHHHH
Number of operations: 7
"""
"""
n = 10
H => Copy All => Paste => HH => Paste-> HHHH -> Paste => HHHHHH -> Paste => HHHHHHHH -> Paste => HHHHHHHHHH
Number of operations: 7
"""


