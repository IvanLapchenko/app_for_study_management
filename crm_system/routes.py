from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from crm_system import app
from crm_system.models.database import session
from crm_system.models.group import Group
from crm_system.models.student import Student
from crm_system.models.user import User


@app.route("/main")
def index():
    return render_template("main.html")


@app.route("/")
@app.route("/group_management", methods=["GET", "POST"])
def group_management():
    all_data = session.query(Group).all()
    all_data = [i.group_name for i in all_data]
    if request.method == "POST":
        group_name = request.form["gr_name"]
        group = Group(group_name=group_name)
        session.add(group)
        session.commit()
        session.close()
        return redirect("group_management")
    return render_template("group_management.html", group_names=all_data)


@app.route("/student_management/<g_name>", methods=["GET", "POST"])
def group_list(g_name):
    gr_id = session.query(Group).where(Group.group_name == g_name).first().id
    group = session.query(Student).where(Student.group == gr_id).all()
    if request.method == "POST":
        surname = request.form["surname"]
        name = request.form["name"]
        age = request.form["age"]
        address = request.form["address"]
        student = Student(surname=surname, name=name, age=int(age), address=address, id_group=gr_id)
        session.add(student)
        session.commit()
        session.close()
        return redirect(f"/student_management/{g_name}")
    return render_template("student_management.html", group=group)


@app.route("/signup")
def signup():
    if request.method == "POST":
        username = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            return redirect(url_for('signup'))

        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))

        session.add(new_user)
        session.commit()
        session.close()

        return redirect("login")
    return render_template("signup.html")