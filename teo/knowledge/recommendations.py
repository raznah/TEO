"""
Scout Recommendation Engine.

This module decides what Scout recommends to the player.
"""

from teo.knowledge.festivals import (
    get_current_festival,
    get_next_festival,
)


def get_recommendation():
    """
    Return Scout's recommendation.

    Returns a dictionary containing:
        - title
        - reason
        - source
    """

    current_festival = get_current_festival()

    if current_festival:

        return {
            "title": f"Enjoy {current_festival['name']}",
            "reason": (
                "A festival is currently active. "
                "This is the best opportunity available today."
            ),
            "source": "Festival Engine"
        }

    next_festival = get_next_festival()

    if next_festival:

        return {
            "title": f"Prepare for {next_festival['name']}",
            "reason": (
                "No festival is currently active. "
                "This is a good opportunity to prepare before it begins."
            ),
            "source": "Festival Engine"
        }

    return {
        "title": "Explore Tyria",
        "reason": (
            "Scout couldn't find any special activities today."
        ),
        "source": "Scout"
    }