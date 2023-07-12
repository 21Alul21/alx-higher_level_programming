#!/usr/bin/python3
""" this  Module contains a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ this Function returns
        an object by a JSON representation
    
    """
    return json.loads(my_str)
