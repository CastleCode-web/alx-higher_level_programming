#!/usr/bin/python3
""" This module contains a function that writes an
    object to a textfile using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a textfile using a JSON
        representation
    """
    with open(filename, mode="w", encoding="utf-8") as MyFile:
        a_file = MyFile.write(json.dumps(my_obj))
        return a_file
