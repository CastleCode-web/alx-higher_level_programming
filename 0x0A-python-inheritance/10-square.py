#!/usr/bin/python3
""" This module contains a Square grandchild which
    inherits from Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ creates a class that inherits from Rectangle """
    def __init__(self, size):
        """ a constructor that instantiates the size private attribute,
            which is validated by integer_validator from BaseGeometry
        """
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)
