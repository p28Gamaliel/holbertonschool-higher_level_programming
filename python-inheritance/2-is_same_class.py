#!/usr/bin/python3
"""
True if the object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    returns:
        True if obj is exactly an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
