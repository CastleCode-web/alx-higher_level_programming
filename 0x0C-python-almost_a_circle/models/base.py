#!/usr/bin/python3
""" This module contains a class with a private class attribute,
    amd class constructor
"""
import json


class Base(object):
    """ creates a class named Base that inherits from object
        superclass
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class constructor that accept id as the only argument
            and sets it to none
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json representation of list_dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string representation to a file """
        files = []
        if list_objs is not None:
            for elem in list_objs:
                files.append(cls.to_dictionary(elem))
        my_file = cls.__name__ + ".json"
        with open(my_file, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(files))
