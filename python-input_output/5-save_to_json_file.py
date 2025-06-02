#!/usr/bin/python3
"""
"""

import json


def save_to_json_file(my_obj, filename):
    """
    """
    with open(filename, "w") as f:
        json_string = json.dumps(my_obj)
        f.write(json_string)
