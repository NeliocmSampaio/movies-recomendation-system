from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .artist_movie import artist_movie_association
from .director_movie import director_movie_association
from .user_movie import user_movie_association


class Movie(Base):
    __tablename__ = 'tab_movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(200))
    release_date = Column(Date)

    artists = relationship(
        "Artist", secondary=artist_movie_association, back_populates="movies")

    directors = relationship(
        "Director", secondary=director_movie_association, back_populates="movies")

    users = relationship(
        "User", secondary=user_movie_association, back_populates="movies")
