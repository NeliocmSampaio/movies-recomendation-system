from ..entities import visualization
from ..entities.visualization import RecomendationModel
from sqlalchemy.orm import Session
from ..entities.visualization import Model
import numpy as np

trained_model = Model()


def train_model(db: Session):
    RecomendationModel.load_history(db)

    model = RecomendationModel.train_recomendation()

    trained_model.df_predictions = model.df_predictions
    trained_model.user_movie_matrix = model.user_movie_matrix


def get_recomendation_for_user(user_id: int):
    recomended = RecomendationModel.recomend_movies(
        user_id=user_id, num_recomendations=3)

    print("User ", user_id)
    for i, (movie_id, pred_rating) in enumerate(recomended.items(), 1):
        print(f"{i}. Movie {movie_id} - Predição de nota: {pred_rating:.1f}")

    recomendation = [(movie, rating) for (movie, rating) in recomended.items()]

    return recomendation
