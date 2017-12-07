def isPrime(i):
    """checks wether i is prime"""

    if i <= 1:
        return False

    if i <= 3:
        return True

    if i % 2 == 0 or i % 3 == 0:
        return False

    return True
