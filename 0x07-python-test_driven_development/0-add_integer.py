#!/usr/bin/python3
"""

    func

"""


def add_integer(a, b=98):
    """
        func
    """
    if type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not int:
        raise TypeError('b must be an integer')
    return a + b
