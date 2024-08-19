from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship


artist_movie_association = Table(
    'tab_artist_movie',
    Base.metadata,
    Column('artist_id', Integer, ForeignKey('tab_artists.id')),
    Column('movie_id', Integer, ForeignKey('tab_movies.id'))
)
