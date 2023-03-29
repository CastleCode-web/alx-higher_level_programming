#!/usr/bin/python3
"""
    Bytecode module to calculate the area
    and circumference of a circle
"""
import math


class MagicClass:
    """
        Creates magic class
    """
    def __init__(self, radius=0):
        """
            instantiate circle attribute
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """
            calculates area of the circle
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
            calculates the circumference of the circle
        """
        return 2 * math.pi * self.__radius
