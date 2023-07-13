#!/usr/bin/python3
# 10-square.py
"""squares that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


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
