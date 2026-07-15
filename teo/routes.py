from flask import Blueprint, render_template

from teo.engine.festivals import (
    get_current_festival,
    get_next_festival,
)

main = Blueprint("main", __name__)


@main.route("/")
def index():

    current_festival = get_current_festival()
    next_festival = get_next_festival()

    return render_template(
        "index.html",
        current_festival=current_festival,
        next_festival=next_festival,
    )