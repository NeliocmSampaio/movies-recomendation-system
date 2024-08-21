from ..entities import visualization
from sqlalchemy.orm import Session


def get_visualization_history(db: Session):
    data = visualization.VisualizationHistory()

    df = data.get_history(db)

    model = data.train_recomendation(df)

    for user_id in range(1, 10):
        recomended = data.recomend_movies(
            user_id=user_id, model=model, num_recomendations=3)

        print("User ", user_id)
        for i, (movie_id, pred_rating) in enumerate(recomended.items(), 1):
            print(f"{i}. Movie {movie_id} - Predição de nota: {pred_rating:.1f}")

    recomended = data.recomend_movies(
        user_id=10, model=model, num_recomendations=5)

    return recomended
