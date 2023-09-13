#!/usr/bin/python3
""" func """


def write_file(filename="", text=""):
    """ func """
    with open(filename, 'w') as f:
        return f.write(text)
