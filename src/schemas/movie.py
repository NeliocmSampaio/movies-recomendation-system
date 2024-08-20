from pydantic import BaseModel
from datetime import datetime, date


class MovieSchema(BaseModel):
    name: str
    description: str
    release_date: date
