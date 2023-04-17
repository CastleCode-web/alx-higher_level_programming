#!/usr/bin/python3
"""
    This module contains MyInt class that
    inherits from it.
"""


class MyInt(int):
    """
        MyInt class inherits from int and acts as a rebel
    """
    def __eq__(self, other):
        """ checks if the instance and other are equal and
            inverse it
        """
        self.other = other
        return self.other != other

    def __ne__(self, other):
        """ checks if the instance and other are not equal
            and inverse it
        """
        self.other = other
        return self.other == other
