"""
Daily Rotation Knowledge

Loads today's Daily Catch rotation.
"""

from teo.knowledge.loader import load_json


def load_daily_rotation():
    """
    Load the Daily Catch rotation.
    """

    return load_json("daily_rotation.json")


def get_daily_rotation():
    """
    Return today's Daily Catch rotation.
    """

    return load_daily_rotation()