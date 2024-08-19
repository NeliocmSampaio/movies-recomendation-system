from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .director_movie import director_movie_association


class Director(Base):
    __tablename__ = 'tab_directors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    movies = relationship(
        'Movie', secondary=director_movie_association, back_populates="directors")
