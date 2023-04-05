#!/usr/bin/python3
"""

This module's class does not 
dynmaically create new attributes

"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ this is the Init method """
        pass
