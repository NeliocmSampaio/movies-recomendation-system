from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])


class Movie(BaseModel):
    name: str


@router.get("/")
def read_root():
    return "Ok"
