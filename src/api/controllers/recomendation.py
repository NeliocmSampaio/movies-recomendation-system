from ...domain.services import recomendation
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...infrastructure.db.dependencies import get_db

router = APIRouter(prefix="/recomendation", tags=["recomendation"])


@router.post("/train")
def handle_train_model(db: Session = Depends(get_db)):
    return recomendation.train_model(db)


@router.post("/get-recomendation/{user_id}")
def handle_get_recomendation(user_id: int):
    return recomendation.get_recomendation_for_user(user_id)
