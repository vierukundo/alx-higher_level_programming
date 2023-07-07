#!/usr/bin/python3
# 0-add_integer.py
"""add_integer function definition"""


def add_integer(a, b=98):
    """adds two integers
    Floats are typecasted to int
    Raises:
        TypeError: if either a or b is not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
