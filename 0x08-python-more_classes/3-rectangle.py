#!/usr/bin/python3
"""
contains a class that define a Rectangle
it contains a __str__ class that returns 
'#' depending on the width and height values
"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width, height):
        
        """ 
        Arguments
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        
        """ 
        this method returns the value of the width
        Returns rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
         this is a  method that defines the width
        Argsuments are;
            value: width
        what to raise:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ 
          this is a method that returns the value of the height
        Returns  rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ 
           defines height
        Args:
            value: height
        what to raise;
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
          Method calculates the Rectangle area
        Returns:
            rectangle area
        """

        return self.width * self.height

    def perimeter(self):
        """ 
        Method calculates the Rectangle perimeter
        Returns:
            rectangle perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height

    def __str__(self):
        """
        a string method that returns 
        # for the width and height values
        of the Rectangle class
        """
        
        if (self.width == 0 or self.height == 0):
            return ""
        else
            i = 1
            b = ""
            while (i <= self.height):
                 b += ('#' * self.width) + "\n"
            return b[:-3]
