#!/usr/bin/python3
"""

moudule that contains a function that adds
two integers and returns their sum

"""


def add_integer(a, b=98):
    """

    :param a: a
    :param b: b
    :return: a + b
    """
    if (type(a)) != int and (type(a)) != float:
        raise TypeError("a must be an integer")
    if (type(b)) != int and (type(b)) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
