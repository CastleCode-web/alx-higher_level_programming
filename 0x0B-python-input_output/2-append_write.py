#!/usr/bin/python3
""" This module contains a function that appends a string
    at the end of a text file and returns the number
    of character added
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file and
        returns the number of character added. If the file
        doesn't exist, it's created
    """
    with open(filename, mode ="a", encoding="utf-8") as MyFile:
        a_file = MyFile.write(text)
        return a_file
