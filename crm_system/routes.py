from flask import render_template, request
from crm_system import app
from crm_system.models.database import session
from crm_system.models.group import Group
from crm_system.models.student import Student


@app.route("/main")
def index():
    return render_template("main.html")


@app.route("/")
@app.route("/group_management", methods=["GET", "POST"])
def group_management():
    groups = session.query(Group)
    if request.method == "POST":
        group_name = request.form["gr_name"]
        student = Group(group_name=group_name)
        session.add(student)
        session.commit()
    return render_template("group_management.html", group_names=groups)


@app.route("/group_list/<g_name>")
def group_list(g_name):
    gr_id = session.query(Group).where(Group.group_name == g_name).first().id
    group = session.query(Student).where(Student.group == gr_id).all()
    return render_template("student_management.html", group=group)

