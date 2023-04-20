#!/usr/bin/python3
""" Module contains a class and a constructor and methods """


class Student(object):
    """ creates a class named Student """
    def __init__(self, first_name, last_name, age):
        """ constructs the first_name, last_name and age attributes of
            the Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retirves the dictionary representation of student instance """
        if attrs == None:
            return self.__dict__
        else:
            attr_dict = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    attr_dict[item] = self.__dict__[item]
            return attr_dict

    def reload_from_json(self, json):
        """ replaces all attributes of student instance """
        for k, v in json.items():
            setattr(self, k, v)
