#!/usr/bin/python3
""" func """


def inherits_from(obj, a_class):
    """ func """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
