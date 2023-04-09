#!/usr/bin/python3
"""

module that contains class that defines a Rectangle


"""


class Rectangle:
    """ rectangle  Class, it defines a rectangle """

    def __init__(self, width=0, height=0):
        """

        Args:
            width: rectangle width
            height: rectangle height


        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ 
           Returns:
           rectangle width


        """

        return self.__width

    @width.setter
    def width(self, value):
        """

        Args:
            value: width

        Raise:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """

        if type(value) != int: 
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns:
            rectangle height


        """

        return self.__height

    @height.setter
    def height(self, value):
        """ 

        Args:
            value: height

        Raise:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ this is the Method used to  calculates the Rectanglearea

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """ this  Method  calculates the Rectangle perimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
