#!/usr/bin/python3
"""convert text, dir, etc in str using Json."""


import json


def to_json_string(my_obj):
    """convert."""
    return json.dumps(my_obj)
