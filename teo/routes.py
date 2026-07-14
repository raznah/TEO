from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return """
    <html>
        <head>
            <title>Tyrian Economic Optimizer</title>
        </head>

        <body style="font-family:Segoe UI; margin:40px;">
            <h1>Tyrian Economic Optimizer</h1>

            <h3>Version 0.1 – Minnow</h3>

            <hr>

            <p>Welcome to TEO.</p>

            <p>The journey begins.</p>
        </body>
    </html>
    """