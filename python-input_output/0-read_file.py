#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file.txt"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
