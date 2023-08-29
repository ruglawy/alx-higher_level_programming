#!/usr/bin/python3
"""Class"""


class Square:
    """Class"""
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        try:
            if size < 0:
                raise ValueError('size must be >= 0')
            self.__size = int(size)
        except TypeError as e:
            raise TypeError('size must be an integer')
