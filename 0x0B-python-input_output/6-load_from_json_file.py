#!/usr/bin/python3
"""Create Object from JSON file"""
import json


def load_from_json_file(filename):
    """a function that reads and parses a JSON object from a file."""
    with open(filename) as rf:
        return json.load(rf)
