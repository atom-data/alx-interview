#!/usr/bin/env python3.4
"""
Defining the function makeChange
"""


def makeChange(coins, total):
    if total == 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    change = total
    for coin in coins:
        count += change // coin
        change = change % coin
        if change == 0:
            return count
    return -1
