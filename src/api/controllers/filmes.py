from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...infrastructure.db.dependencies import get_db
from ...crud.movie import create_movie, get_movies, get_movie
from pydantic import BaseModel
from typing import List
from ...domain.services import recomendation

router = APIRouter(prefix="/filmes", tags=["filmes"])


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


@router.get("/{user_id}/recomendacoes")
def handle_get_movie(user_id,
                     db: Session = Depends(get_db)) -> MovieResponse:
    return recomendation.get_recomendation_for_user(user_id)
