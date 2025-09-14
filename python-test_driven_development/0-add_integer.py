#!/usr/bin/python3
"""
Module that provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Args:
        a (int or float): first number.
        b (int or float): second number, defaults to 98.

    Raises:
        TypeError: If a or b is not an int or float.

    Returns:
        int: Sum of a and b.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer
    >>> add_integer(3.7, 2.3)
    5
    >>> add_integer(-1, -2)
    -3
    >>> add_integer(0, 0)
    0
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
