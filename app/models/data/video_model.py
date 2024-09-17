from sqlalchemy import Column, Integer, String

from app.helpers.database_helper import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    author = Column(String, index=True)
    duration = Column(Integer)
    src = Column(String)
    topic = Column(String)