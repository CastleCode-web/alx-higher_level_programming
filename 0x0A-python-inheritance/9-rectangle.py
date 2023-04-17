#!/usr/bin/python3
""" Module contains a child class that inherits from
    BaseGeometry, the area() is implemented and a str()
    is created
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ a subclass that inherits the superclass,
        BaseGeometry
    """
    def __init__(self, width, height):
        """ A constructor that instantiates the width and
            height attributes
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """ overrides the area() in the superclass and
            makes it calculate the area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ returns the string representation of the
            Rectangle instances
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
