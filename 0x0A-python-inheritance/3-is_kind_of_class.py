#!/usr/bin/python3

"""

  This module contains a function
  that returns boolean True of
  False is the arguments are of
  the same type

"""


def is_kind_of_class(obj, a_class):
    """
    takes two arguments( the object and the class)
    returns True or False if the
    arguments are of the same class or the same
    inherited class

    """

    return isinstance(obj, a_class)
