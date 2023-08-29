#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0,0)):
        """initialize square
        Args:
            size (int): size
            position (tuple): position
        """
        self.size = size
        self.position = position

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
            raise TypeError('size must be integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """idk

        Return:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets new position
        Args:
            value (tuple): position
        """
        if type(value) is not tuple or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >=0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """calculate area

        Return:
            area
        """
        return self.__size**2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
