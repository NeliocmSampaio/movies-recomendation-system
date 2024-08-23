from pydantic import BaseModel
from datetime import datetime, date


class DirectorSchema(BaseModel):
    name: str
