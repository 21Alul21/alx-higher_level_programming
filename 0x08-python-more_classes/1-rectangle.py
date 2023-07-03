#!/usr/bin/python3
"""
module that contains a class that 
has two instant variables 
with properties set using the @property and
@setter decorators.

"""

class Rectangle:
"""retrieves the rectangle parameters and set it"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return __self.width

    @width.setter
    def width(self, value):
        if not isinstance(self.width, int):
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")
        __self.width = value 
           

