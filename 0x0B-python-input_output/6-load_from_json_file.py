#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """create a python3 object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
