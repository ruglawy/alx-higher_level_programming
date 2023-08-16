#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keylist = list(a_dictionary)
    for key in keylist:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary.copy()
