import uuid
from sqlalchemy.orm import Session
from ..schemas.movie import MovieSchema
from ..domain.entities.movie import Movie
from ..infrastructure.db.models.movie import MovieModel
from typing import List


def get_movies(db: Session) -> List[Movie]:
    data = db.query(MovieModel).all()
    return data


def get_movie(db: Session, movie_id) -> Movie:
    return db.query(MovieModel).filter(MovieModel.id == movie_id).first()


def create_movie(db: Session, movieSchema: MovieSchema) -> Movie:
    movie = MovieModel(name=movieSchema.name, description=movieSchema.description,
                       release_date=movieSchema.release_date)

    db.add(movie)
    db.commit()

    return Movie(
        id=movie.id,
        name=movie.name,
        description=movie.description,
        release_date=movie.release_date
    )
