#!/usr/bin/python3
"""

Say me name

"""


def say_my_name(first_name, last_name=""):
    """ Func

    Args:
        first_name: name
        last_name: name

    Returns:
        No return

    Raises:
        TypeError: If first_name or last_name is not a string


    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
