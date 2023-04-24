#!/usr/bin/python3
""" Module contains a rectangle class that inherit from base
    super class
"""
from models.base import Base


class Rectangle(Base):
    """ creates a class named Rectangle that inherits from
        base super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ a constructor for the Rectangle class that
            instantiates its private attributes. it accepts
            5 arguments, the width, height, x, y and the id
            from Base class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ returns the width attribute """ 
        return self.width

    @width.setter
    def width(self, value):
        """ assign a value to the width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    @property
    def height(self):
        """ returns the height attribute """
        return self.height

    @height.setter
    def height(self, value):
        """ assigns a value to the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = value

    @property
    def x(self):
        """ returns the x attribute """
        return self.x

    @x.setter
    def x(self, value):
        """ assign a value to the x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = value

    @property
    def y(self):
        """ returns the y attribute """
        return self.y

    @y.setter
    def y(self, value):
        """ assign a value to y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = value
