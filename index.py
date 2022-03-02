from random import random
import string
import random
from flask import render_template, Flask, jsonify, request


app = Flask(__name__)


# @app.route("/")
# def index():
#     return "hello world"


@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/things")
async def things():
    letters = string.ascii_lowercase
    data = "".join(random.choice(letters) for i in range(64))
    return jsonify({"data": data})


@app.route("/things/<int:id>")
async def thing_id(id):
    return jsonify({"thing_id": id})


# /item?color=red
@app.route("/item")
async def index():
    color = request.args.get("color")
    return {"color": color}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
