from flask import Blueprint, render_template

from teo.knowledge.festivals import (
    get_current_festival,
    get_next_festival,
)

from teo.knowledge.daily_catch import get_daily_catch

from teo.reasoning.scout import get_daily_recommendation

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """
    Render the TEO dashboard.
    """

    current_festival = get_current_festival()
    next_festival = get_next_festival()

    recommendation = get_daily_recommendation()

    daily_catch = get_daily_catch()

    return render_template(
        "index.html",
        current_festival=current_festival,
        next_festival=next_festival,
        recommendation=recommendation,
        daily_catch=daily_catch,
    )