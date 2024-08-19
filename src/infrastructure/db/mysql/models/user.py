from ..mysql import Base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from .user_movie import user_movie_association


class User(Base):
    __tablename__ = 'tab_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(50), unique=True)
    name = Column(String(100))


    movies = relationship(
        'Movie', secondary=user_movie_association, back_populates="users")