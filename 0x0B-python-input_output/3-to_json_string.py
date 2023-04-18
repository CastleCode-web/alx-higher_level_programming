#!/usr/bin/python3
""" This module contains a function that returns the
    JSON representation of a string
"""
import json


def to_json_string(my_obj):
    """ A function that returns the JSON
        representation of a string
    """
    return json.dumps(my_obj)
