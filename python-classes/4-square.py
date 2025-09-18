#!/usr/bin/python3
"""we define the class"""


class Square:
    """asuca"""

    def __init__(self, size=0):
        """
        initiating exceptions.

        raises:

        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        2.
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
