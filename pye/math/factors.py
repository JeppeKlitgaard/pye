from math import sqrt


def factors(num):
    """Returns the factors of 'num' in a set.

    This is a slow and inefficient pure-python implementation.
    Should do just fine for most use-cases, but if you have to calculate a
    lot of numbers, you might want to find an alternative.

    :Parameters:
        - `num` The number to be factorized.

    :Returns Type:
        set

    :Examples:
    >>> factors(10)
    set([1, 10, 2, 5])
    >>> factors(7)
    set([1, 7])
    >>> factors(123257654)
    set([1, 2, 4740679, 13, 9481358, 123257654, 26, 61628827])"""
    factors = []

    for i in range(1, int(sqrt(num)) + 1):  # For number in sqrt
        if num % i == 0:  # If is divisible with no remainder.
            factors.append(i)  # Append number
            factors.append(num // i)  # Append number divided with seed-number

    return set(factors)  # Return in a set to remove duplicates
