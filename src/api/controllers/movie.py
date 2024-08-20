
import uuid
from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..requests.movie_requests import MovieRequest
from ...infrastructure.db.dependencies import get_db
from ...infrastructure.db.models.movie import MovieModel
from ...schemas.movie import MovieSchema
from ...crud.movie import create_movie, get_movies, get_movie
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
def handle_get_movies(db: Session = Depends(get_db)) -> List[MovieResponse]:
    data = get_movies(db)
    return data


@router.get("/{movie_id}")
def handle_get_movie(movie_id,
                     db: Session = Depends(get_db)) -> MovieResponse:
    return get_movie(db, movie_id)


@router.post("/")
def handle_create_movie(movieRequest: MovieRequest,
                        db: Session = Depends(get_db)) -> MovieResponse:
    movie = MovieSchema(
        **movieRequest.model_dump()
    )

    return create_movie(db, movie)
