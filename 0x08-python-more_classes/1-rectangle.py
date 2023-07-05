#!/usr/bin/python3
# 1-main.py
"""Rectangle class defintion"""


class Rectangle:
    """representation Rectangle"""
    def __init__(self, width=0, height=0):
        """Instance initialization
        args:
            width(int): width of rectangle
            height(int): height of rectangle
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """retrieves width"""
        return self.__width
    @width.setter
    def width(self, value):
        """sets width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """retrieves height"""
        return self.__height
    @height.setter
    def height(self, value):
        """sets height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
