import datetime
from collections import defaultdict
from flask import Blueprint, render_template, request, url_for, redirect

pages = Blueprint(
    "habits",__name__, template_folder="templates", static_folder="static"
)
habits = ["Test Habit"]
completions = defaultdict(list)


@pages.context_processor
def add_calc_date_range():
    def date_range(start: datetime.datetime):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates
    return {"date_range": date_range}

@pages.route("/")
def day():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.datetime.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()

    return render_template("day.html", habits=habits, title="Day a Day", selected_date=selected_date, completions=completions[selected_date])


@pages.route("/complete", methods=["POST"])
def complete():
    date_string = request.form.get("date")
    habit = request.form.get("habitId")
    date = datetime.datetime.fromisoformat(date_string)
    completions[date].append(habit)

    return redirect(url_for(".day", date=date_string))



@pages.route("/add", methods=["GET", "POST"])
def add_day():
    if request.form:
      habits.append(request.form.get("habit"))

    return render_template("add_day.html", title="Day a day - Add", selected_date=datetime.date.today(),)

