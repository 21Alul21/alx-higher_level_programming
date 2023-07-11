#!/usr/bin/python3
"""
  This module contains a  Class that inherits
  from class int

"""


class MyInt(int):
    """ This Class inherits from class int"""

    def __eq__(self, other):
        """ This Method returns != check """

        return int.__ne__(self, other)

    def __ne__(self, other):
        """ This Method  returns == check """

        return int.__eq__(self, other)
