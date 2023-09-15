#!/usr/bin/python3
""" CLASS """


class Base:
    """ CLASS """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = __nb_objects
