from pathlib import Path
import json

RESOURCE_PATH = (
    Path(__file__).resolve().parent.parent
    / "resources"
    / "daily_catch.json"
)


def load_daily_catch():
    """
    Load the Daily Catch database.
    """

    with open(RESOURCE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def get_daily_catch():
    """
    Return the Daily Catch information.

    Returns None if no data exists.
    """

    data = load_daily_catch()

    if not data:
        return None

    return data