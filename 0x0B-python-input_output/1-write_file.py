#!/usr/bin/python3
""" This module contains a function that writes a string
    to a text file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Writes a string to a textfile and returns the number
        of characters written
    """
    with open(filename, mode = "w", encoding = "utf-8") as MyFile:
        a_file = MyFile.write(text)
        return a_file
