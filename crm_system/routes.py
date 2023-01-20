from flask import render_template, request
from crm_system import app
from crm_system.models.database import session, database
from crm_system.models.group import Group
from crm_system.models.student import Student


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/group_management", methods=["GET", "POST"])
def group_management():
    groups = session.query(Group)
    if request.method == "POST":
        group_name = request.form["gr_name"]
        student = Group(group_name=group_name)
        session.add(student)
        session.commit()
    return render_template("group_management.html", groups=groups)