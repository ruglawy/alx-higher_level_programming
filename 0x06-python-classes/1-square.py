#!/usr/bin/python3
"""Class"""


class Square:
    __size = None

    def __init__(self, size = None):
        if size is not None:
            self.__size = size
