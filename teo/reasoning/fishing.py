"""
Fishing Reasoning

Uses Scout's knowledge to generate fishing recommendations.
"""

from teo.knowledge.daily_rotation import get_daily_rotation
from teo.knowledge.fish_species import get_fish


def get_fishing_recommendation():
    """
    Build today's fishing recommendation.
    """

    rotation = get_daily_rotation()

    if not rotation:
        return None

    routes = rotation.get("routes", {})

    if "janthir_syntri" not in routes:
        return None

    fish_id = routes["janthir_syntri"]["required_fish_id"]

    fish = get_fish(fish_id)

    if not fish:
        return None

    return {
        "title": "Today's Daily Catch",
        "priority": 100,
        "activity": "Fishing",
        "target": fish["name"],
        "reason": "Current Daily Catch",
        "preparation": [
            "Equip the recommended bait.",
            "Equip your best lure.",
            "Use fishing food.",
            "Fish from your skiff.",
            "Build Fishing Party stacks.",
            "Complete the Fishing and Skiff mastery tracks."
        ],
        "knowledge": fish
    }