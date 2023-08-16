#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = list(map(lambda x, y: x if x == y else pass, set_1, set_2))
    return set(set_3)
