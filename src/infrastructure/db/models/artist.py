from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .artist_movie import artist_movie_association


class ArtistModel(Base):
    __tablename__ = 'tab_artists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    movies = relationship(
        'MovieModel', secondary=artist_movie_association, back_populates="artists")
