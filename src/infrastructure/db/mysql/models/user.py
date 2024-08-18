from ..mysql import Base
from sqlalchemy import Column, Integer, String, Numeric


class User(Base):
    __tablename__ = 'tab_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(50), unique=True)
    name = Column(String(100))
