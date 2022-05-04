from flask import Flask, render_template, request, jsonify, flash, redirect
import json, datetime
from models.school import School
from models.homework import Homework


app = Flask(__name__)

# Home page that loads the data in a table
@app.route("/")
def homepage():
    with open(r"data\homework.json", "r") as fp:
        data = json.load(fp)
    return render_template("home.html", homeworkdata=data), 200

# Brings up the create page with the forms
@app.route("/create")
def createpage():
    return render_template("create.html"), 200

# Displays all the homework in a JSON format
@app.route("/homework", methods=["GET"])
def stupage():
    with open(r"data\homework.json", "r") as fp:
        data = json.load(fp)
        return jsonify(data), 200

# Homework endpoint for POST, takes course, type, description, and due date from the forms from the /create endpoint
@app.route("/homework", methods=["POST"])
def create_student():
    # Getting course, type, description, and due date
    course = request.form.get("course")
    name = request.form.get("name")
    type = request.form.get("type")
    desc = request.form.get("description")
    dd = request.form.get("duedate")
    #dd = get_date()

    # Creating the school to place all the homework in  
    school = School("BCIT")

    try:
        # Adding the homework to the school
        homework = Homework(course, name, type, desc, dd)
        school.add(homework)
        school.save()
        return "Homework added", 201
        # If theres a value error returns 400 error
    except ValueError:
        return "Invalid parameters", 400


def get_date():
    # get date in field in YYYY-MM-DD format
    date_valid = request.form.get("duedate")
    try:
        datetime.datetime.strptime(date_valid, '%Y-%m-%d')
    except ValueError:
        flash("Please enter date as YYYY-MM-DD")
        return redirect("/create")      # just goes to error page, idk how to redirect back?

    return str(date_valid)


if __name__ == "__main__":
    app.run(debug=True)
