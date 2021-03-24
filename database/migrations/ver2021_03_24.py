import os
from database.migrations import Base
from sqlalchemy import create_engine
import database.entities.task
import database.entities.schedule
import database.entities.worker
import database.entities.assignment

USER = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]
HOST = os.environ["HOST"]
NAME = os.environ["NAME"]


def create_database():
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}/{NAME}')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
