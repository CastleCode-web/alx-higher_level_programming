#!/usr/bin/python3
""" This module contains a class with a private class attribute,
    amd class constructor
"""


class Base(object):
    """ creates a class named Base that inherits from object
        superclass
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class constructor that accept id as the only argument
            and sets it to none
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = Base.__nb_objects
