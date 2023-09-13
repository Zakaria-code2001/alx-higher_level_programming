#!/usr/bin/python3
"""DEFINES A STRING TO JSON FUNCTION."""
import json


def to_json_string(my_obj):
    """RETURN THE JSON REPRESENTATION OF A STRING OBJECT."""
    return json.dumps(my_obj)
