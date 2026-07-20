"""
Scout

Scout presents recommendations produced by the reasoning engine.
"""

from teo.reasoning.engine import get_top_recommendation


def get_daily_recommendation():
    """
    Return today's best recommendation.
    """

    recommendation = get_top_recommendation()

    if recommendation is None:
        return {
            "title": "Scout",

            "message": "I don't have any recommendations yet."
        }

    message = (
        f"I recommend today's Daily Catch: "
        f"{recommendation['target']}."
    )

    return {
        "title": recommendation["title"],

        "message": message,

        "recommendation": recommendation
    }