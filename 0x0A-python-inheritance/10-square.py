#!/usr/bin/python3
"""
   This module contains a Class that
   defines a Square from Rectangle class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ this Class defines a Square from Rectangle class """
    def __init__(self, size):
        """ this  Method initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()
