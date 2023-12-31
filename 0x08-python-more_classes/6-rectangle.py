#!/usr/bin/python3
"""
class ...
"""


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """return value"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """return rectangle with characters of #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = ""
        for i in range(self.__height):
            for j in range(self.__width):
                shape += "#"
            if i < self.__height - 1:
                shape += "\n"
        return shape

    def __repr__(self):
        """return string rep for rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
