import uuid
from sqlalchemy.orm import Session
from ..schemas.movie import movieSchema
from ..domain.entities.movie import Movie
from ..infrastructure.db.models.movie import Movie
from typing import List


def get_movies(db: Session) -> List[movie]:
    return db.query(movie).all()


def get_movie(db: Session, movie_id) -> movie:
    return db.query(movie).filter(movie.id == movie_id).first()


def create_movie(db: Session, movieSchema: movieSchema) -> movie:
    movie_uuid = uuid.uuid4()
    movie = movie(name=movieSchema.name, uuid=str(movie_uuid))

    db.add(movie)
    db.commit()

    return movie
