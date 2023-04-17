#!/usr/bin/python3
""" contains a class that inherits from list """


class MyList(list):
    """ a class that inherits from list and contains
        a method that prints the sorted list
    """
    def print_sorted(self):
        """ prints the list in sorted order """
        print(sorted(self))
