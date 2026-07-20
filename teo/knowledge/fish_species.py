"""
Fish Species knowledge module.

Provides access to the fish species knowledge base.
"""

import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "resources" / "fish_species.json"


def load_fish_species():
    """
    Load the fish species database.

    Returns:
        dict: Fish species data.
    """

    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)