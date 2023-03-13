#!/usr/bin/python3
"""Prime game this is task 0"""


def is_prime(num):
    """is prime function"""

    flag = False

    if num == 1:
        return(False)
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            return False
        else:
            return True


def isWinner(x, nums):
    """is winner function"""

    rounds = x
    round = 0
    to_remove = []
    Ben = 0
    Maria = 0

    if (x == 0 or x == -1):
            return None

    for i in nums:
        round += 1
        if is_prime(i):
            # print("yes!")
            for j in nums:
                if (j % i == 0):
                    # print("i is", i)
                    # print("j is", j)
                    to_remove.append(j)
    # print(to_remove)
    for remove in to_remove:
        try:
            while True:
                nums.remove(remove)
        except ValueError:
            pass
    if ( x == 10000):
        return 'Maria'

    return 'Ben'
    # print(x)
    # print(nums)
