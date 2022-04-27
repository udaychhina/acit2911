from multiprocessing.sharedctypes import Value
from flask import Flask, render_template, request, jsonify
import json


app = Flask(__name__)

@app.route("/")
def homepage():
    with open(r"data\homework.json", "r") as fp:
        data = json.load(fp)
    return render_template("home.html", homeworkdata=data), 200




if __name__ == "__main__":
    app.run(debug=True)
