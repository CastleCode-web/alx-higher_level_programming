#!/usr/bin/python3
""" This module contains a class and a method """


class BaseGeometry(object):
    """ a class that contains a method that throws an exception
        each time it's called
    """
    def area(self):
        """ a method that raises an exception """
        raise Exception("area() is not implemented")
