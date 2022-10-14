import datetime
from select import select
from collections import defaultdict
from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app=Flask(__name__)
    completions = defaultdict(list) 



    @app.context_processor
    def add_calc_date_range():
        def date_range(start: datetime.date):
            dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
            return dates
        return {"date_range": date_range}
    
    habits = []

    @app.route("/")
    def day():
        date_str = request.args.get("date")
        if date_str:
            selected_date = datetime.date.fromisoformat(date_str)
        else:
            selected_date = datetime.date.today()
        
        return render_template("day.html", habits=habits, title="Day a Day", selected_date=selected_date, completions=completions[selected_date])


    @app.route("/add", methods=["GET", "POST"])
    def add_day():
        if request.method == "POST":
            habits.append(request.form.get("habit"))
        return render_template("add_day.html", title="Day a day - Add", selected_date=datetime.date.today())

    @app.route("/complete", methods=["POST"])
    def complete():
        date_string = request.form.get("date")
        habit = request.form.get("habitname")
        date = datetime.date.fromisoformat(date_string)
        completions[date].append(habit)

        return redirect(url_for("day", date=date_string))


    return app