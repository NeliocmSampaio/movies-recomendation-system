
import uuid
from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..requests.movie_requests import MovieRequest
from ...infrastructure.db.mysql.dependencies import get_db
from ...infrastructure.db.mysql.models.movie import Movie
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/movies", tags=["movies"])


class MovieResponse(BaseModel):
    name: str
    description: str
    release_date: date

    class Config:
        orm_mode = True


@router.get("/")
def get_movies(db: Session = Depends(get_db)) -> List[MovieResponse]:
    return db.query(Movie).all()


@router.get("/{movie_id}")
def get_movie(movie_id,
              db: Session = Depends(get_db)) -> MovieResponse:
    return db.query(Movie).filter(Movie.id == movie_id).first()


@router.post("/")
def add_movie(movieRequest: MovieRequest,
              db: Session = Depends(get_db)) -> MovieResponse:
    movie_uuid = uuid.uuid4()
    movie = Movie(
        **movieRequest.model_dump()
    )

    db.add(movie)
    db.commit()

    return movie
