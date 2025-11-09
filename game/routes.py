from flask import render_template,  request, session, redirect, url_for
from game import app



@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [None,None,None],[None,None,None],[None,None,None]
        session["turn"] = "x"
    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row,col):
    return redirect(url_for("index"))

