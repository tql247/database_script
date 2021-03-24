from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.types import DateTime, Integer, Text

from database.migrations import Base


class Schedule(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    priority = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=True)
    deadline = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)

    create_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
