#!/usr/bin/python3
"""Module 11-square
Defines a Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
