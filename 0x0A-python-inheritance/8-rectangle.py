#!/usr/bin/python3
""" This module contains Rectangle class,
    a child class that inherits from the BaseGeometry
    parent class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ a child class that inherits from BaseGeometry parent
        class, has a width and height constructor which must be
        validated by integer_validator() from BaseGeometry
    """
    def __init__(self, width, height):
        """ constructor of width and height attributes
            which must be integers, both are validated through
            integer_validator method in the superclass
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
