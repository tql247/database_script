import os
from datetime import datetime
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.types import Date, DateTime, Integer, Time
from sqlalchemy import Integer, Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None


class Manga(Base):
    __tablename__ = 'manga'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    image_cover_thumbnail_uri = Column(String, nullable=False)
    manga_name = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    deleted_at = Column(DateTime, nullable=True)


class MangaDetail(Base):
    __tablename__ = 'manga_detail'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    manga_id = Column(Integer, ForeignKey('manga.id'), nullable=False)
    image_cover_uri = Column(String, nullable=False)
    alternative = Column(String, nullable=False)
    author_s = Column(String, nullable=False)
    tags = Column(String, nullable=False)
    description = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    deleted_at = Column(DateTime, nullable=True)


class MangaProvider(Base):
    __tablename__ = 'manga_provider'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    manga_id = Column(Integer, ForeignKey('manga.id'), nullable=False)
    provider_uri = Column(String, nullable=True)


class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    manga_id = Column(Integer, ForeignKey('manga.id'), nullable=False)
    chapter_index = Column(Integer, nullable=False)
    chapter_name = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    deleted_at = Column(DateTime, nullable=True)


class ChapterProvider(Base):
    __tablename__ = 'chapter_provider'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    chapter_id = Column(Integer, ForeignKey('chapter.id'), nullable=False)
    provider_uri = Column(String, nullable=True)


class ChapterDetail(Base):
    __tablename__ = 'chapter_detail'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    chapter_provider = Column(Integer, ForeignKey('chapter_provider.id'), nullable=False)
    page_index = Column(Integer, nullable=False)
    chapter_content_uri = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    deleted_at = Column(DateTime, nullable=True)


def get_db_url():
    USER = os.environ["USER"]
    PASSWORD = os.environ["PASSWORD"]
    HOST = os.environ["HOST"]
    DB_NAME = os.environ["DB_NAME"]
    return f'postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}'


def create_database():
    global engine

    db_url = get_db_url()
    engine = create_engine(db_url)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    sess = Session(engine)
    sess.commit()
