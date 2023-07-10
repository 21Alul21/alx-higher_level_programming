#!/usr/bin/python3
"""
 This module contains a
 a class that inherits from
 the inbuilt class 'list'
 so, it automatically converts its objects to a
 list, then it has a method that sorts the list
"""


class MyList(list):
    """

    This class contains a function
    that inherits a list and
    returns the sorted form of that list.

    """

    def print_sorted(self):
        """

         This function takes the list as an argument,
         makes a copy,
         sorts it, and prints the sorted format.


        """

        list_sorted = self[:]
        list_sorted.sort()
        print(list_sorted)

