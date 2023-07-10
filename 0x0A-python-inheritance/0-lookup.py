#!/usr/bin/python3
"""

 This module contains a 
 a function that returns the list 
 of available attributes and methods of an object

"""


def lookup(obj):
    """

    this function takes the object as
    an argument 
    and returns a list containing the available 
    attributes and methods of the object

    """

    return dir(obj)
