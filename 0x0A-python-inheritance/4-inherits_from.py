#!/usr/bin/python3
""" contains a function that checks
    if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """ checks if the object is an instance of a
        class that inherited (directly or indirectly)
        from the specified class
    """
    if type(obj) != a_class:
        return True
    return False
