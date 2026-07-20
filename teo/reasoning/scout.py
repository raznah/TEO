"""
Scout reasoning engine.

Scout combines knowledge and current state to produce recommendations.
"""

from teo.knowledge.daily_catch import load_daily_catch
from teo.knowledge.daily_rotation import load_daily_rotation
from teo.knowledge.fish_species import load_fish_species


def get_daily_recommendation():
    """
    Generate Scout's first recommendation.

    Returns:
        dict: Recommendation information for the dashboard.
    """

    daily_catch = load_daily_catch()
    rotation = load_daily_rotation()
    fish = load_fish_species()

    return {
        "title": "Scout's Recommendation",
        "message": (
            "Good morning! I've explored Tyria and gathered today's "
            "Daily Catch information."
        ),
        "daily_catch": daily_catch,
        "daily_rotation": rotation,
        "fish_species": fish,
    }