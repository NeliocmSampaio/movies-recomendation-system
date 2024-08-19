from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship


director_movie_association = Table(
    'director_movie',
    Base.metadata,
    Column('director_id', Integer, ForeignKey('tab_directors.id')),
    Column('movie_id', Integer, ForeignKey('tab_movies.id'))
)
