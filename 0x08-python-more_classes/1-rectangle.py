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
    """ retrieves the value """
        return self.__width

    @width.setter
    def width(self, value):
    """ sets the value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value 
          
    @property
    def height(self):
    """ retrieves the value """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
