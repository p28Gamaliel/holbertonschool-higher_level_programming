#!/usr/bin/python3
"""JSON format using json.dump()."""


import json


def save_to_json_file(my_obj, filename):
    """save."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
