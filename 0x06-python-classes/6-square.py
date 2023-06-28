#!/usr/bin/python3
# 6-square.py
"""square class definition"""


class Square:
    """Representation of square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of class instance
        args:
            size(int): size of square
            position(tule): coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if i < 0 or not isinstance(i, int):
                    raise TypeError(
                            "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area"""
        return self.__size * self.__size

    def my_print(self):
        """prints square with character #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

