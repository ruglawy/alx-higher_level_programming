#!/usr/bin/python3
"""Class"""


class Square:
    """Class zeft"""
    def __init__(self, size = None):
        """initialize square
        Args:
            size (int): size of the square
        """
        if size is not None:
            self.__size = size
