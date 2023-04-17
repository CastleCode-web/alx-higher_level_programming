#!/usr/bin/python3
""" contains a function that checks if an object is an
    instance of or that of a class that inherited from the
    specified class
"""


def is_kind_of_class(obj, a_class):
    """ checks if an object is an instance of or that of a
        class that inherited from the specified class
    """
    if isinstance(obj, a_class):
        return True
    return False
