from flask import Flask, render_template, request
from model import detect_items
from recipes import get_recipes
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    items = []
    recipes = []

    if request.method == "POST":
        file = request.files["image"]
        if file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)

            items = detect_items(path)
            recipes = get_recipes(items)

    return render_template("index.html", items=items, recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)