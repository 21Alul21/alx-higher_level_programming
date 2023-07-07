#!/usr/bin/python3
"""

    this module contains a function that indents
    a line or nlock of text whenever
    certain characters like ".?:" are encontered

"""


def text_indentation(text):
    """

       this function indents a line
       or block of code once ".?:"
       charaters are encountered

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
