#!/usr/bin/python3
"""
Define isWinner function
"""


def modified_sieve(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, True

    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n + 1) if primes[i]]

def isWinner(x, nums):
    max_num = max(nums)
    primes = modified_sieve(max_num)

    score = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = sum((i in primes) for i in range(n + 1))
        if prime_count % 2 == 0:
            score["Maria"] += 1
        else:
            score["Ben"] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"
    else:
        return None

