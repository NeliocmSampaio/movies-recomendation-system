import uuid
from sqlalchemy.orm import Session
from ..schemas.user import UserSchema
from ..domain.entities.user import User
from ..infrastructure.db.models.user import UserModel
from typing import List


def get_users(db: Session) -> List[User]:
    return db.query(UserModel).all()


def get_user(db: Session, user_id) -> User:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(db: Session, userSchema: UserSchema) -> User:
    user_uuid = uuid.uuid4()
    user = UserModel(name=userSchema.name, uuid=str(user_uuid))

    db.add(user)
    db.commit()

    return User(
        id=user.id,
        uuid=user.uuid,
        name=user.name
    )
