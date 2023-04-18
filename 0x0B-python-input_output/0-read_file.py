#!/usr/bin/python3
""" This module contains a function that reads a text
    file and prints it to stdout
"""


def read_file(filename=""):
    """ reads a text file and prints it to stdout """
    with open(filename, mode = "r", encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
