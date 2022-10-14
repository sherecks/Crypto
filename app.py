from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app=Flask(__name__)


    habits = []

    @app.route("/")
    def day():
        return render_template("day.html", habits=habits, title="Day a Day")


    @app.route("/add", methods=["GET", "POST"])
    def add_day():
        if request.method == "POST":
            habits.append(request.form.get("habit"))
        return render_template("add_day.html", title="Day a day - Add")

    return app