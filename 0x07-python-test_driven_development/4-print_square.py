#!/usr/bin/python3
"""


module that contains function that prints
a square using the character "#"


"""


def print_square(size):
    """

       this function prints a square using #
       for every iteration made

   
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
