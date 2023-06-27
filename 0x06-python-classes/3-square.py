#!/usr/bin/python3
# 3-square.py
""" class defination called square"""


class Square:
    """representation of square"""
    def __init__(self, size=0):
        """Initialization of instance of class
        args:
            size(int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns square area"""
        return self.__size ** 2
