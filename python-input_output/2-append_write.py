#!/usr/bin/python3
"""append write."""


def append_write(filename="", text=""):
    """append new string."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)