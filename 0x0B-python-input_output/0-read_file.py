#!/usr/bin/python3
""" func """


def read_file(filename=""):
    """ func """
    with open(filename) as f:
        data = f.read()
        print(data, end='')
