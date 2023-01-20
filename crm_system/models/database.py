from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = 'app.db'

database = create_engine(f'sqlite:///{db_name}')
Session = sessionmaker(bind=database)
session = Session()

Base = declarative_base()


def create_db():
    Base.metadata.create_all(database)