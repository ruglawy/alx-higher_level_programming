#!/usr/bin/python3
"""Class Square"""


class Square:
    """initialize square"""
    def __init__(self, size):
        """initialize square
        Args:
            size (int): size
        """
        if type(size) is not int:
            raise TypeError('size must be integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Get area
        Args:
            none
        Return:
            area
        """
        return self.__size * self.__size
