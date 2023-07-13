#!/usr/bin/python3
# 4-inherits_from.py
"""definition of function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False"""
    obj_actual_class = obj.__class__
    if issubclass(obj_actual_class, a_class) and obj_actual_class != a_class:
        return True
    return False
