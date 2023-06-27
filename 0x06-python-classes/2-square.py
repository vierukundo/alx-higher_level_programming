#!/usr/bin/python3
# 2-square.py
""" class defination called square"""

class Square:
    """a class Square that defines a square by
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    """
    def __init__(self, size=0):
        """Initialization of instance of class
        args:
            size(int): size of square
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
        except(TypeError, ValueError):
            raise
        self.__size = size
