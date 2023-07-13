#!/usr/bin/python3
# 11-square.py
Rectangle = __import__('9-rectangle').Rectangle
"""squares that inherits from Rectangle"""


class Square(Rectangle):
    """square representation"""
    def __init__(self, size):
        """instance initialization
        args:
            size(int): size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """arear of square"""
        return (self.__size ** 2)

    def __str__(self):
        """returns string representation of class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
