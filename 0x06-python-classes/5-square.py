#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size
        """
        self.size = size

    @property
    def size(self):
        """idk

        Return:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets new size
        Args:
            value (int): size of square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate area

        Return:
            area
        """
        return self.__size**2

    def my_print(self):
        """Print

        Return:
            none
        """
        if size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
