from flask import render_template
from task_manager import app, db
from task_manager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")