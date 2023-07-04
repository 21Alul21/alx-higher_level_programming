"""

 module contains a function that
outputs first and last name
entered as arrguments

"""


def say_my_name(first_name, last_name=""):
    """

    :param first_name: "Austin"
    :param last_name: "Alul"
    :return: Austin Alul

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))I
