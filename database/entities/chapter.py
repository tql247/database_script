from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, DateTime, Integer, Time

from database.migrations import Base
from sqlalchemy import MetaData

metadata_obj = MetaData()


class Schedule(Base):
    __tablename__ = 'chapter'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    schedule_id = Column(Integer, ForeignKey('schedule.id'), nullable=False)
    worker_id = Column(Integer, ForeignKey('worker.id'), nullable=False)
    task_id = Column(Integer, ForeignKey('task.id'), nullable=False)

    create_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
