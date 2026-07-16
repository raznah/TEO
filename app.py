from teo import create_app

app = create_app()

from teo.knowledge.festivals import get_current_festival

print(get_current_festival())


if __name__ == "__main__":
    app.run(debug=True)