#!/usr/bin/python3
# 10-student.py
"""defines student to json class"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialization of student objects
        args:
            first_name(str): first name
            last_name(str): last name
            age(int): age
        returns:
            dictionary representation of a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        args:
            attrs: attributes names
        Returns:
            dictionary representation
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                try:
                    new_dict[key] = self.__dict__[key]
                except KeyError:
                    continue
        return new_dict
