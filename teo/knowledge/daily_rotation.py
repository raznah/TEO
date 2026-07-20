"""
Daily Rotation knowledge module.

Provides access to today's Daily Catch rotation.
"""

import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "resources" / "daily_rotation.json"


def load_daily_rotation():
    """
    Load today's Daily Catch rotation.

    Returns:
        dict: Daily rotation data.
    """

    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)