#!/usr/bin/python3
"""

Function

"""


def print_square(size):
    """ Func

    Args:
        size: size

    Returns:
        No return

    Raises:
        TypeError: If size is not int


    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print ("#" * size)
