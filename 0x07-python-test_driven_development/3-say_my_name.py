#!/usr/bin/python3
'''
This module contains a afunction that
prints string characters to stdout
'''


def say_my_name(first_name, last_name=""):
    '''
    say_my_name is a function that prints the first and
    last names of users in string format
    '''
    if not type(first_name) is str:
        raise TypeError("{} must be a string".format(first_name))
    if not type(last_name) is str:
        raise TypeError("{} must be a string".format(last_name))
    print("My name is {:s} {:s}".format(first_name, last_name))
