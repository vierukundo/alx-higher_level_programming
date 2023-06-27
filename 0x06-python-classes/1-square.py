#!/usr/bin/python3
# 1-square.py
"""Define a square class"""


class Square:
    """class Square that defines a square by
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """
        This is --init-- documentation
        args:
            size: size of square and should be private
        """
        self.__size = size
