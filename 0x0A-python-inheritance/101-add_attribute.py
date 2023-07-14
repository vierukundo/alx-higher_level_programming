#!/usr/bin/python3
# 101-add_attribute.py
"""ffunction definition"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it's possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, attr, value)
