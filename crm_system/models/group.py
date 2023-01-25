from sqlalchemy import Column, Integer, String


from crm_system.models.database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String)


    # def __repr__(self):
    #     return f"{self.group_name}"
