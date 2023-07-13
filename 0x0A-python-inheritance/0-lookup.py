#!/usr/bin/python3
# 0-lookup.py
"""definition of lookup function"""


def lookup(obj):
    """returns the list of available attributes
    and methods of an object"""
    return (dir(obj))
