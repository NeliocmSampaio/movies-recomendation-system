from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .artist_movie import artist_movie_association
# from .director_movie import director_movie_association
from .user_movie import user_movie_association


class MovieModel(Base):
    __tablename__ = 'tab_movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(200))
    release_date = Column(Date)
    genre = Column(String(30))
    director_id = Column(Integer, ForeignKey("tab_directors.id"))

    artists = relationship(
        "ArtistModel", secondary=artist_movie_association, back_populates="movies")

    directors = relationship(
        "DirectorModel", back_populates="movies")

    users = relationship(
        "UserModel", secondary=user_movie_association, back_populates="movies")
