from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base
from flask_login import UserMixin


class Student(UserMixin, Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)
    group = Column(Integer, ForeignKey('groups.id'))
    username = Column(String(100), unique=True)
    password = Column(String(100))

    def __init__(self, name: str, surname: str, age: int, address: str, id_group: int, username: str, password: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.address = address
        self.group = id_group
        self.username = username
        self.password = password


    # def __repr__(self):
    #     info = f"self.surname, self.name, self.age, self.address, self.group"
    #     return info
