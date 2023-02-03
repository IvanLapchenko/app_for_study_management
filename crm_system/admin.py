from models.database import session
from models.group import Group
from models.student import Student
from werkzeug.security import generate_password_hash

g = Group(group_name="test")
s = Student(surname="admin", name="admin", age=111, address="admin", id_group="admin", username="admin", password=generate_password_hash("admin"))

session.add(g)
session.commit()
session.add(s)
session.commit()
