#!/usr/bin/python3
""" func """


def append_write(filename="", text=""):
    """ func """
    with open(filename, 'a') as f:
        return f.write(text)
