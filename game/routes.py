from flask import render_template, sessions, request
from game import app


@app.route("/")
def home():
    return render_template("game.html")
