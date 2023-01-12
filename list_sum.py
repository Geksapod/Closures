""" This module provide access to list_sum function"""
from typing import Callable


def list_sum(num_list: list, func: Callable[[list], list]):
    """
    This function return link to the calculate function.

    :param num_list: The list of numbers.
    :param func: The applied function to each member of the list.
    """

    def calculate():
        """
        This function applied an arbitrary user function to each member of the list and return sum of them.
        The list and the arbitrary user function are parameters of the outer list_sum function.
        """

        for index, num in enumerate(num_list):
            num_list[index] = func(num)
        return sum(num_list)

    return calculate
