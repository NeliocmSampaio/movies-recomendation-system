from pydantic import BaseModel
from datetime import datetime, date


class MovieRequest(BaseModel):
    name: str
    description: str
    release_date: date
