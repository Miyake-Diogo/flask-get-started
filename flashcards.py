from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

count = 0
@app.route("/count_views")
def count_views():
    global count
    count += 1
    return "This page was viewed at " + str(count)  + " times."