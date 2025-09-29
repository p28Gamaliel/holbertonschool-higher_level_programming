#!/usr/bin/python3
"""Module 9-rectangle
Defines a Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
