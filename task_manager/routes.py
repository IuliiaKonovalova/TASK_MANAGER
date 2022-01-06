from flask import render_template
from task_manager import app, db


@app.route("/")
def home():
    return render_template("base.html")