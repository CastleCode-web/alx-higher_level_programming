#!/usr/bin/python3
""" Module contains a class, a constructor and methods """


class Student(object):
    """ creates a class named Student and is inherited from object """
    def __init__(self, first_name, last_name, age):
        """ constructs the attributes of the Student class, these are
            first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves the dictionary representation of Student """
        return self.__dict__
