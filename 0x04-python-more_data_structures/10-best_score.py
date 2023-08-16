#!/usr/bin/python3
def best_score(a_dictionary):
    keylist = list(a_dictionary)
    if len(keylist) == 0:
        return None
    max_num = a_dictionary[keylist[0]]
    for key in keylist:
        if a_dictionary[key] > max_num:
            max_num = a_dictionary[key]
    return max_num
