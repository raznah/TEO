"""
Scout Reasoning Engine

The engine gathers recommendations from every reasoning module,
prioritizes them, and returns the best recommendation.
"""

from teo.reasoning.fishing import get_fishing_recommendation


def get_recommendations():
    """
    Collect recommendations from every reasoning module.
    """

    recommendations = []

    fishing = get_fishing_recommendation()

    if fishing:
        recommendations.append(fishing)

    recommendations.sort(
        key=lambda recommendation: recommendation["priority"],
        reverse=True
    )

    return recommendations


def get_top_recommendation():
    """
    Return the highest-priority recommendation.
    """

    recommendations = get_recommendations()

    if recommendations:
        return recommendations[0]

    return None