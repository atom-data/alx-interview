#!/usr/bin/python3
"""
Define isWinner function
"""


def isWinner(x, nums):
    primes = []
    winner_lst = []
    max_elem = max(nums)
    numbers = [i for i in range(1, max_elem + 1)]

    for i in range(1, len(numbers)):
        for j in numbers[i + 1:].copy():
            if j % numbers[i] == 0:
                numbers.remove(j)

    for k in nums.copy():
        for l in numbers.copy():
            if l <= k:
                primes.append(l)
        psize = len(primes)
        if psize % 2 == 0:
            winner_lst.append('Maria')
        else:
            winner_lst.append('Ben')
        primes.clear()

    bcount = winner_lst.count('Ben')
    wsize = len(winner_lst)
    if bcount > (wsize - bcount):
        most_freq = 'Ben'
        count_diff = bcount - (wsize - bcount)
    else:
        most_freq = 'Maria'
        count_diff = (wsize - bcount) - bcount

    if count_diff > (x - wsize) or (x - wsize) == 0:
        return most_freq
    else:
        return None
