#!/usr/bin/python3
# 9-rectangle.py
"""Rectangle class defintion"""


class Rectangle:
    """representation Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instance initialization
        args:
            width(int): width of rectangle
            height(int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print the message Bye rectangle..."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
                s += str(self.print_symbol) * self.__width
            else:
                s += str(self.print_symbol) * self.__width + '\n'
        return s

    def __repr__(self):
        """return a string representation of the rectangle to be
        able to recreate a new instance by using eval()"""
        return "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
