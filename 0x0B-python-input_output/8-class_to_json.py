#!/usr/bin/python3
""" Module contains a function that returns the dictionary
    description with simple data structure list for JSON
    serialization of an object
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
        list for JSON object serialization. obj is an instance of a class
    """
    return obj.__dict__
