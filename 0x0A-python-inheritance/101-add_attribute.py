#!/usr/bin/python3
""" This module contains a method that adds
    a new attribute to an object. If attribute can't
    be added, it raises a TypeError
"""


def add_attribute(cls, attr, value):
    """ creates a method that adds attribute to objects.
        It takes three arguments,
        cls-> the class that creates the object
        attr-> the attribute to add
        value-> the value of the attribute
        The object must have a __dict__ to work
    """
    """ Print(dir(cls))
        print(cls.__dict__)
        print(help(cls.__setattr__))
    """
    if ("__dict__" in dir(cls)):
        setattr(cls, attr, value)
    else:
        raise TypeError("can't add new attribute")
