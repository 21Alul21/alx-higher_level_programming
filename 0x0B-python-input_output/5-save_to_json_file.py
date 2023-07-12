#!/usr/bin/python3
"""this  Module writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ this Function writes an object to a text file
    by a JSON representation
    """

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
