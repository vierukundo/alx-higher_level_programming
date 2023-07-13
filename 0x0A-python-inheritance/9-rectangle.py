#!/usr/bin/python3
# 9-rectangle.py
"""importing base class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representation of rectangle"""
    def __init__(self, width, height):
        """Initialization of an instance
        args:
            width(int): width
            height(int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns string representation of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
