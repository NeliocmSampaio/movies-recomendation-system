from pydantic import BaseModel
from datetime import datetime, date
from .director import Director
from .artist import Artist
from typing import List


class Movie(BaseModel):
    id: int
    name: str
    description: str
    release_date: date
    director: Director
    artists: List[Artist]
