#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            print(result.strip())
            print()
            result = ""
        i += 1
    if result:
        print(result.strip(), end="")
