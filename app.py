from turtle import title
from unicodedata import name
from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def index();
    return render_template("day.html", title="Day a Day")