#!/usr/bin/python3
# 4-square.py
"""square class definition"""


class Square:
    """Representation of square"""
    def __init__(self, size=0):
        """initialization of class instance
        args:
            size(int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area"""
        return self.__size * self.__size
