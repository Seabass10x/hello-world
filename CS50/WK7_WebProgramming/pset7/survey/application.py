import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    # Server side validation of form submission
    if not request.form.get("title") or not request.form.get("firstName") or not request.form.get("lastName") or not request.form.get("house"):
        return render_template("error.html", message="You must complete all fields of the form!")

    # Open csv file in append mode
    file = open("survey.csv", "a")
    writer = csv.writer(file)

    # Append fields from form to csv file
    writer.writerow((request.form.get("title"), request.form.get("firstName"),
                     request.form.get("lastName"), request.form.get("house")))
    file.close()
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # return render_template("error.html", message="I haven't coded the sheet html yet")

    # Open csv in read mode
    file = open("survey.csv", "r")
    reader = csv.reader(file)

    # Place records in a list
    records = list(reader)
    return render_template("sheet.html", records=records)
