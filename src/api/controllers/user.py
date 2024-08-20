import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..requests.user_request import UserRequest
from ...infrastructure.db.dependencies import get_db
from ...infrastructure.db.models.user import User
from ...schemas.user import UserSchema
from ...crud.user import create_user, get_user, get_users
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/user", tags=["user"])


class UserResponse(BaseModel):
    name: str
    uuid: str

    class Config:
        orm_mode = True


@router.get("/")
def handle_get_users(db: Session = Depends(get_db)) -> List[UserResponse]:
    return get_users(db)


@router.get("/{user_id}")
def handle_get_user(user_id,
                    db: Session = Depends(get_db)) -> UserResponse:
    return get_user(db, user_id)


@router.post("/")
def handle_create_user(userRequest: UserRequest, db: Session = Depends(get_db)) -> UserResponse:
    user = UserSchema(name=userRequest.name)

    return create_user(db, user)
