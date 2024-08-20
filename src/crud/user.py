import uuid
from sqlalchemy.orm import Session
from ..schemas.user import UserSchema
from ..domain.entities.user import User
from ..infrastructure.db.models.user import User
from typing import List


def get_users(db: Session) -> List[User]:
    return db.query(User).all()


def get_user(db: Session, user_id) -> User:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, userSchema: UserSchema) -> User:
    user_uuid = uuid.uuid4()
    user = User(name=userSchema.name, uuid=str(user_uuid))

    db.add(user)
    db.commit()

    return user
