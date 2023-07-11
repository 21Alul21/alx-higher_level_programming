#!/usr/bin/python3
""" This module contains Class that defines a rectangle from BaseGeometry Class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The Rectangle Class defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ This Method returns the area of the instance"""

        return self.__width * self.__height

    def __str__(self):
        """ this is a Special method that returns the printable string """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
