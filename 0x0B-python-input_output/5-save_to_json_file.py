#!/usr/bin/python3
""" func """
import json


def save_to_json_file(my_obj, filename):
    """ func """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
