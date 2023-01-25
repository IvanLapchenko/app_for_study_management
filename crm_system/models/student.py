from sqlalchemy import Column, Integer, String, ForeignKey

from crm_system.models.database import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name: list[str], age: int, address: str, id_group: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.age = age
        self.address = address
        self.group = id_group

    # def __repr__(self):
    #     info = f"self.surname, self.name, self.age, self.address, self.group"
    #     return info
