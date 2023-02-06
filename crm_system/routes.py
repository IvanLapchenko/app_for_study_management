from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import app, login_manager
from .models.database import session
from .models.group import Group
from .models.student import Student


@app.route("/")
@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/group_management")
def user_group():
    all_data = session.query(Group).all()
    all_data = [i.group_name for i in all_data]
    return render_template("group_management.html", group_names=all_data)


@app.route("/group_management", methods=["POST"])
@login_required
def group_management():
    group_name = request.form["gr_name"]
    group = Group(group_name=group_name)
    session.add(group)
    session.commit()
    session.close()
    return redirect("group_management")


@app.route("/student_management/<g_name>")
def user_group_list(g_name):
    gr_id = session.query(Group).where(Group.group_name == g_name).first().id
    group = session.query(Student).where(Student.group == gr_id).all()
    group = {i.name:i.surname for i in group}
    return render_template("student_management.html", group=group)


@app.route("/student_management", methods=["POST"])
@login_required
def group_list():
    surname = request.form["surname"]
    name = request.form["name"]
    age = request.form["age"]
    address = request.form["address"]
    username = request.form["username"]
    password = request.form["password"]
    gr_id = request.form["group"]

    student = Student(surname=surname, name=name, age=int(age), address=address, id_group=gr_id, username=username, password=password)
    session.add(student)
    session.commit()
    session.close()

    return redirect("/admin")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('name')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = session.query(Student).where(Student.username == username).first()

        if not user or not check_password_hash(user.password, password):
            print(user)
            print(check_password_hash(user.password, password))
            flash('Please check your login details and try again.')
            return redirect(url_for("login"))

        login_user(user, remember=remember)
        return redirect(url_for("main"))

    return render_template("login.html")


@app.route("/admin")
def admin():
    groups = session.query(Group).all()
    groups = [i.group_name for i in groups]
    return render_template("admin.html", groups=groups)


@app.route("/profile")
def profile():
    gr_name = session.query(Group).where(Group.id == current_user.group).first().group_name
    name = current_user.name
    lessons = ["mock1", "mock2"]
    print(current_user.id)
    return render_template("profile.html", name=name, gr_name=gr_name, lessons=lessons)
    #todo add getting student id and his data by it 
    #i believe we should usr current_user.id or something


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))


@login_manager.user_loader
def load_user(user_id):
    return session.query(Student).get(int(user_id))
