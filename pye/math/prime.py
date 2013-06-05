from math import sqrt


def is_prime(num):
    """Returns True if num is a prime, otherwise returns False.

    This is a slow and inefficient pure-python implementation.
    Should do just fine for most use-cases, but if you have to calculate a
    lot of numbers, you might want to find an alternative.

    :Parameters:
        - `num` The number to be checked.

    :Returns Type:
        bool

    :Examples:
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True"""
    num = abs(int(num))  # Make sure num is positive.

    # 0 and 1 are not primes.
    if num < 2:
        return False

    if num == 2:
        return True

    # All even numbers (except 2) are not primes.
    if not num & 1:
        return False

    # Range starts with 3, and only needs to go up to the squareroot of num
    # Go in steps of two, since all other even numbers are non-prime
    for x in range(3, int(sqrt(num)) + 1, 2):
        if num % x == 0:
            return False

    return True
