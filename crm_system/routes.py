from flask import render_template
from crm_system import app


@app.route("/")
def index():
    return render_template("main.html")
