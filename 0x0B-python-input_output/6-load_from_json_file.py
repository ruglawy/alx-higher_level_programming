#!/usr/bin/python3
""" func """
import json


def load_from_json_file(filename):
    """ func """
    with open(filename) as f:
        return json.load(f)
