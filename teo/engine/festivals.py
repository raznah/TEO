from datetime import datetime
from pathlib import Path
import json

RESOURCE_PATH = (
    Path(__file__).resolve().parent.parent
    / "resources"
    / "festivals.json"
)


def load_festivals():
    """Load the festival database."""

    with open(RESOURCE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
        

def get_current_festival(today=None):
    """
    Return the currently active festival.

    Returns None if no festival is active.
    """

    if today is None:
        today = datetime.today().date()

    festivals = load_festivals()

    for festival in festivals:

        start = datetime.strptime(
            festival["start"],
            "%Y-%m-%d"
        ).date()

        end = datetime.strptime(
            festival["end"],
            "%Y-%m-%d"
        ).date()

        if start <= today <= end:
            return festival

    return None
    
    
def get_next_festival(today=None):
    """
    Return the next upcoming festival.

    Returns None if no future festivals exist.
    """

    if today is None:
        today = datetime.today().date()

    festivals = load_festivals()

    upcoming = []

    for festival in festivals:

        start = datetime.strptime(
            festival["start"],
            "%Y-%m-%d"
        ).date()

        if start > today:

            upcoming.append((start, festival))

    if not upcoming:
        return None

    upcoming.sort(key=lambda item: item[0])

    start_date, festival = upcoming[0]

    festival = festival.copy()

    festival["days_remaining"] = (start_date - today).days

    return festival