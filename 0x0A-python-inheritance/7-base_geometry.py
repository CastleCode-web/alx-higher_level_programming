#!/usr/bin/python3
""" contains a class with two methods.
    the area() which raises an area exception, and
    integer_validator() that validates value
"""


class BaseGeometry(object):
    """ creates a class that contains two methods,
        the area() and integer_validator()
    """
    def area(self):
        """ raises an area exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates value. If value is not an integer,
            it raises error, if value is <= 0, it also raises error
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
