#!/usr/bin/python3
"""
module that contains a class that 
has two instant variables 
with properties set using the @property and
@setter decorators.

"""


class Rectangle:
    """
       retrieves the rectangle
       parameters and set it
       to a defined custom value

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ 

        method that retrieves the value for the width
        and and makes it private

        """
        return self.__width

    @width.setter
    def width(self, value):
        """ 

        method that sets the value for the height
        and and makes it private

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value 
          
    @property
    def height(self):
        """ 

        method that retrieves the value for the width
        and and makes it private

        """
        return self.__height

    @height.setter
    def height(self, value):
        """ 

        method that sets the value for the height
        and and makes it private

        """
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.height < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
