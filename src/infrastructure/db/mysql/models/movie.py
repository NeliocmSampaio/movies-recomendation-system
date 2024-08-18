from ..mysql import Base
from sqlalchemy import Column, Integer, String, Date


class Movie(Base):
    __tablename__ = 'tab_movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(200))
    release_date = Column(Date)
