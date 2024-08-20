from .user import User
from .artist import Artist
from .director import Director
from .movie import Movie
from sqlalchemy.orm import Session
from typing import List
from ...infrastructure.db.models.user import UserModel
from ...infrastructure.db.models.movie import MovieModel
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import ratings


class Visualization:
    user: User
    movie: Movie


class VisualizationHistory:
    log: List[Visualization]

    def get_history(self, db: Session):
        users = db.query(UserModel).all()

        data = []
        for user in users:
            for movie in user.movies:
                data.append(
                    {
                        "user_id": user.id,
                        "movie_id": movie.id,
                        "director": movie.director_id,
                        "artists": [artist.id for artist in movie.artists]
                    }
                )

        df = pd.DataFrame(data)
        print(df)

        mlb_artists = MultiLabelBinarizer()
        artists_encoded = mlb_artists.fit_transform(df["artists"])

        df_artists = pd.DataFrame(
            artists_encoded, columns=mlb_artists.classes_)

        df = pd.concat([df, df_artists], axis=1)

        df.drop(columns=["artists"], inplace=True)

        print(df)

        # (training, test) = ratings.randomSplit([0.8, 0.2])
        # als = ALS(maxIter=5, regParam=0.01, userCol="user_id",
        # itemCol = "movie_id", ratingCol = "", coldStartStrategy="drop")
