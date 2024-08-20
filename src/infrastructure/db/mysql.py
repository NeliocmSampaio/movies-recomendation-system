from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import text

from ...core.config import Config, db_config

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{db_config.username}:{
    db_config.password}@{db_config.server}:{db_config.port}/{db_config.name}"
print("con_string: ", SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
