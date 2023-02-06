from models.database import session
from models.group import Group
from models.student import Student
from werkzeug.security import generate_password_hash

g = Group(group_name="test")
s = Student(surname="test1", name="test1", age=111, address="test1", id_group=1, username="test1", password=generate_password_hash("admin"))

session.add(g)
session.commit()
session.add(s)
session.commit()
