from sqlalchemy.orm import Session
from ..schemas.director import DirectorSchema
from ..domain.entities.director import Director
from ..infrastructure.db.models.director import DirectorModel
from typing import List


def get_directors(db: Session) -> List[Director]:
    data = db.query(DirectorModel).all()
    return data


def get_director(db: Session, director_id) -> Director:
    return db.query(DirectorModel).filter(DirectorModel.id == director_id).first()


def create_director(db: Session, directorSchema: DirectorSchema) -> Director:
    director = DirectorModel(name=directorSchema.name)

    db.add(director)
    db.commit()

    return Director(
        id=director.id,
        name=director.name,
    )
