#!/usr/bin/python3
"""convert a text or directory into a string (lista, dict, etc)."""


import json


def from_json_string(my_str):
    """convert."""
    return json.loads(my_str)
