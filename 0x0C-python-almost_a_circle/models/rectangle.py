#!/usr/bin/python3
# rectangle.py
"""definition of rectangle class"""
from models.base import Base


class Rectangle(Base):
    """representation of rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of instance
        args:
            width: width
            height: height
            x: x coordinate
            y: y coordinate
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """changes the value of width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """changes the value of height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """changes the value of x to value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """changes the value of y to value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        height = 0
        while height < self.__height:
            while self.__y > 0:
                print("")
                self.__y -= 1
            print((' ' * self.__x) + ('#' * self.__width))
            height += 1

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[" + self.__class__.__name__ + "] (" + str(
            self.id) + ") " + str(self.__x) + "/" + str(
                self.__y) + " - " + str(
                    self.__width) + "/" + str(self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
