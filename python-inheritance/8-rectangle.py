#!/usr/bin/python3
"""Defines BaseGeometry and Rectangle classes
"""

class BaseGeometry:
    """Base class with area and integer validation"""

    def area(self):
        """Raises an exception if not implemented in subclass"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer

        Args:
            name (str): The name of the variable
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
