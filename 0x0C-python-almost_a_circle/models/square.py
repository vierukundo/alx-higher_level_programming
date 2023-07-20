#!/usr/bin/python3
# square.py
"""defines Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """representationof a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of square instances
        args:
            size(int): width or heidht or size of square
            x(int): coordinate
            y(int): y coorsinate
            id(int or None): number of instances
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] (" + str(self.id) + ") " + str(
            self.x) + "/" + str(self.y) + " - " + str(self.width))

    @property
    def size(self):
        """rreturns size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size to new value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square"""
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
