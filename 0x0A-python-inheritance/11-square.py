#!/usr/bin/python3
""" Module contains a grandchild that inherits
    from the Rectangle class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ creates a class that inherits from Rectangle class """
    def __init__(self, size):
        """ a constructor that instantiates the size private attribute """
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)
        super().area()

    def __str__(self):
        """ returns the string represntation of the square instance """
        return "[Square] {}/{}".format(self.__size, self.__size)
