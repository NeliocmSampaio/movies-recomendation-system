from pydantic import BaseModel


class Director(BaseModel):
    id: int
    name: str
