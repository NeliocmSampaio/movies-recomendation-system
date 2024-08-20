from pydantic import BaseModel


class User(BaseModel):
    id: int
    uuid: str
    name: str
