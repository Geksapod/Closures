""" This module provide access to fibonacci functions"""


def fibonacci_memo():
    """
    Return n-member of the fibonacci sequence.
    """

    fib_numbers = {}

    def n_member(n: int):

        if n in fib_numbers:
            return fib_numbers[n]

        if n == 1 or n == 2:
            num = 1
        elif n > 2:
            num = n_member(n - 1) + n_member(n - 2)
            fib_numbers[n] = num

        return num

    return n_member


def fibonacci_recur(n: int):
    """
    Return n-member of the fibonacci sequence.
    """

    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)
