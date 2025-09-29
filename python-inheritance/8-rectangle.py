#!/usr/bin/python3
"""BaseGeometry."""


class BaseGeometry:
    """
    A base class for geometric shapes.
    """

def integer_validator(name, value):
    """
    Validates that a value is a positive integer.

    Args:
        name (str): The name of the attribute being validated (e.g., "width", "height").
        value (int): The value to validate.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is not a positive integer.
    """
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be > 0")

class Rectangle:
    """
    Represents a rectangle with private width and height attributes.
    Width and height are validated to be positive integers during instantiation.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Must be a positive integer.
            height (int): The height of the rectangle. Must be a positive integer.
        """
        integer_validator("width", width)
        integer_validator("height", height)
        self.__width = width
        self.__height = height
