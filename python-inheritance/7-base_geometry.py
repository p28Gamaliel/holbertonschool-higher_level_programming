#!/usr/bin/python3
"""BaseGeometry."""


class BaseGeometry:
    """
    A base class for geometric shapes.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer
        
        Args:
            name (str): The name of the parameter
            value (int): The value to validate
        
        raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
