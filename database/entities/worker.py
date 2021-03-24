from sqlalchemy import Column, String
from sqlalchemy.types import Integer, Time

from database.migrations import Base


class Worker(Base):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String, nullable=False)
    other_name = Column(String, nullable=True)
    role = Column(Time, nullable=False)
    status = Column(String, nullable=False)
