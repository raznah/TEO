"""
Shared JSON loader for the TEO knowledge layer.
"""

import json
from pathlib import Path


RESOURCES = Path(__file__).parent.parent / "resources"


def load_json(filename):
    """
    Load a JSON file from the resources directory.
    """

    with open(RESOURCES / filename, "r", encoding="utf-8") as file:
        return json.load(file)