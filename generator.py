""" This module provide access to gen function"""
from typing import Callable


def gen(first: int, numbers: int, func: Callable[[int], int]) -> int:
    """
    This is generator function that yields one by one member of a sequence of integers
    and applies an arbitrary user function to each member of the sequence.

    :param first: The first number of sequence generated of this function.
    :param numbers: The numbers of generated members by this function.
    :param func: The applied function to each member of a generated sequence.
    """

    number = 0
    while number < numbers:
        res = yield func(first + number)
        if res:
            numbers = res
        number += 1






