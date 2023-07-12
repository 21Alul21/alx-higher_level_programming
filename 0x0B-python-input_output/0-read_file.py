#!/usr/bin/python3
""" This module contains a function
that reads the content of a text file
"""


def read_file(filename=""):
    """ Function that prints ou
        t the content of a text file
    """

    with open(filename, mode="r", encoding="utf-8") as tf:
        content = tf.read()
        print(content, end="")
