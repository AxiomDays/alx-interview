#!/usr/bin/python3
"""
Script that determines the winner of
a prime game
"""

def isWinner(x, nums):
    """
    x: number of rounds
    nums: array consisting of numbers
    """

    """
    winrate for Ben and Maria
    """

    BenWR=0
    MariaWR=0

    for val in nums:
        if val == 0: continue
        temp_arr = list(range(1, val+1))
        prime_field = sealOfOrichalcos(val)
        if (len(prime_field) % 2 == 0):
            MariaWR += 1
        elif (len(prime_field) % 2 == 1):
            BenWR += 1

    if BenWR > MariaWR:
        return "Ben"
    elif MariaWR > BenWR:
        return "Maria"
    else:
        return None

def sealOfOrichalcos(n):
    """
    function that returns a list of prime numbers
    """

    ret = []
    prime = [True for i in range(n+1)]
    p = 2

    while (p * p <= n):
        if (prime[p] == True):

            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for j in range(1, n+1):
        if prime[j]:
            ret.append(j)
    return ret
