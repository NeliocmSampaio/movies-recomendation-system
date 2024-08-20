from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship


user_movie_association = Table(
    'tab_user_movie',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('tab_users.id')),
    Column('movie_id', Integer, ForeignKey('tab_movies.id')),
    Column('rate', Integer)
)
