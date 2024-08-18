import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..requests.user_request import UserRequest
from ...infrastructure.db.mysql.dependencies import get_db
from ...infrastructure.db.mysql.models.user import User
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/user", tags=["user"])


class UserResponse(BaseModel):
    name: str
    uuid: str

    class Config:
        orm_mode = True


@router.get("/")
def get_users(db: Session = Depends(get_db)) -> List[UserResponse]:
    return db.query(User).all()

@router.get("/{user_id}")
def get_user(user_id,
             db: Session = Depends(get_db)) -> UserResponse:
    return db.query(User).filter(User.id == user_id).first()

@router.post("/")
def create_user(userRequest: UserRequest,
                db: Session = Depends(get_db)) -> UserResponse:
    user_uuid = uuid.uuid4()
    user = User(name=userRequest.name, uuid=str(user_uuid))

    db.add(user)
    db.commit()

    return user
