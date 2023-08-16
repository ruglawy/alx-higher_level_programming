#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    keylist = list(a_dictionary)
    for key in keylist:
        b_dictionary[key] *= 2
    return b_dictionary
