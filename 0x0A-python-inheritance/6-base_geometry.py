#!/usr/bin/python3
"""

This module contains a class
BaseGeometry which contains a
function with an Exception

"""


class BaseGeometry:
    """ This is the Base Geometry class """
    pass

    def area(self):
        raise Exception("area() is not implemented")
