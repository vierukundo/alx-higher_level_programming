#!/usr/bin/python3
# 5-rectangle.py
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

    def __del__(self):
        """Print the message Bye rectangle..."""
        print("Bye rectangle...")

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

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns  rectangle with the character #"""
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for i in range(self.__height):
            if i == self.__height - 1:
                s += '#' * self.__width
            else:
                s += '#' * self.__width + '\n'
        return s

    def __repr__(self):
        """return a string representation of the rectangle to be
        able to recreate a new instance by using eval()"""
        return "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
