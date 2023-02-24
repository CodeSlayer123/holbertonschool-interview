#!/usr/bin/python3
'''Making change algo'''


def makeChange(coins, total):
    '''Making change algo'''

    new_total = total
    change = 0
    coins.sort(reverse=True)
    if (new_total - coins[0] >= 0):
        new_total -= coins[0]
        change += 1
    for coin in coins:
        while(1):
            if (new_total - coin >= 0 and new_total - coin >= coin):
                new_total -= coin
                change += 1
            else:
                break
    if (new_total > 1):
        return -1
    return change