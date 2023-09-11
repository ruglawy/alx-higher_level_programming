#!/usr/bin/python3
""" class """


class MyList(list):
    """ class """
    def print_sorted(self):
        """ func """
        for el in self.sort():
            print(el)
