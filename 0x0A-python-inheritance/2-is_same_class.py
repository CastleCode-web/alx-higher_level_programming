#!/usr/bin/python3
""" contains function that checks if an object is an
    instance or not
"""


def is_same_class(obj, a_class):
    """ checks if an object is an instance or not """
    if type(obj) == a_class:
        return True
    return False
