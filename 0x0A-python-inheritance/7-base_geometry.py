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
        """ method that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value)<0:
            raise ValueError("{} must be greater than 0".format(name))
