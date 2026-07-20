"""
Fish Species Knowledge

Loads fish information used by Scout.
"""

from teo.knowledge.loader import load_json


def load_fish_species():
    """
    Load the fish species knowledge base.
    """

    return load_json("fish_species.json")


def get_fish_species():
    """
    Return every fish.
    """

    return load_fish_species()["fish"]


def get_fish(fish_id):
    """
    Return a fish by ID.
    """

    fish = get_fish_species()

    for entry in fish:
        if entry["fish_id"] == fish_id:
            return entry

    return None