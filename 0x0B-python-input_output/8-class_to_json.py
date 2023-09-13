#!/usr/bin/python3
""" func """


def class_to_json(obj):
    """ func """
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
