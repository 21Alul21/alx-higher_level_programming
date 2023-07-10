#!/usr/bin/python3

"""

   this module contains a function
   that checks and returns true
   or false if an object is an
   instances of a class
"""


def inherits_from(obj, a_class):
    """

       takes two arguments
       and checks it the object is
       an instance of the class


    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
