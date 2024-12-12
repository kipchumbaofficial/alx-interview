#!/usr/bin/python3
""" Prime Game Algorithm
"""


def check_prime(n):
    """ Checks if n is a prime number
    """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def calculate_primes(n, prime):
    """ Calculate all primes
    """
    the_prime = prime[-1]
    if n > the_prime:
        for i in range(the_prime + 1, n + 1):
            if check_prime(i):
                prime.append(i)
            else:
                prime.append(0)


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """

    players_wins = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for round in range(x):
        sum_options = sum((i != 0 and i <= nums[round])
                          for i in primes[:nums[round] + 1])

        if (sum_options % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
