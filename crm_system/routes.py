from flask import render_template, request
from crm_system import app
from crm_system.models.database import session, database
from crm_system.models.group import Group





@app.route("/")
def index():
    return render_template("main.html")


@app.route("/group_management", methods=["GET", "POST"])
def group_management():
    if request.method == "POST":
        gr_name = request.form["gr_name"]
        student = Group(surname = "some",    name = "some",    age = 15,    address = "addr",    )
        session.add(student)
        session.commit()
    return render_template("group_management.html", groups=[1,2])