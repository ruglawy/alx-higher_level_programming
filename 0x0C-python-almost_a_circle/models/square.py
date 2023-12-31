#!/usr/bin/python3
""" CLASS """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ CLASS """
    def __init__(self, size, x=0, y=0, id=None):
        """ initalize """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    @override
    def __str__(self):
        """ str """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ update """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                    continue
                if key == "size":
                    self.size = value
                    continue
                if key == "x":
                    self.x = value
                    continue
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dict """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
