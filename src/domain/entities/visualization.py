from .user import User
from .artist import Artist
from .director import Director
from .movie import Movie
from sqlalchemy.orm import Session
from sqlalchemy import select, Column, Integer
from typing import List
from ...infrastructure.db.models.user import UserModel
from ...infrastructure.db.models.user_movie import user_movie_association
from ...infrastructure.db.models.movie import MovieModel
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Visualization:
    user: User
    movie: Movie


class Model:
    df_predictions: pd.DataFrame
    user_movie_matrix: pd.DataFrame


class RecomendationSystem:
    model: Model
    visualization_history: pd.DataFrame

    def load_history(self, db: Session):
        users = db.query(UserModel).all()

        data = []
        for user in users:
            for movie in user.movies:
                rating = db.query(user_movie_association.c.rate).filter_by(
                    user_id=user.id, movie_id=movie.id).scalar()

                data.append(
                    {
                        "user_id": user.id,
                        "movie_id": movie.name,
                        "director": movie.director_id,
                        "artists": [artist.id for artist in movie.artists],
                        "rating": rating
                    }
                )

        self.visualization_history = pd.DataFrame(data)

        mlb_artists = MultiLabelBinarizer()
        artists_encoded = mlb_artists.fit_transform(
            self.visualization_history["artists"])

        df_artists = pd.DataFrame(
            artists_encoded, columns=mlb_artists.classes_)

        self.visualization_history = pd.concat(
            [self.visualization_history, df_artists], axis=1)

        self.visualization_history.drop(columns=["artists"], inplace=True)

        return self.visualization_history

    def train_recomendation(self):

        user_movie_matrix = self.visualization_history.pivot_table(
            index='user_id', columns='movie_id', values='rating')
        user_movie_matrix.fillna(0, inplace=True)

        movies_similarity = cosine_similarity(user_movie_matrix.T)
        prediction_matrix = np.dot(user_movie_matrix, movies_similarity)

        normalization_factor = np.array(
            [np.abs(movies_similarity).sum(axis=1)])
        prediction_matrix = prediction_matrix / normalization_factor

        df_prediction = pd.DataFrame(
            prediction_matrix, index=user_movie_matrix.index, columns=user_movie_matrix.columns)

        self.model = Model()
        self.model.df_predictions = df_prediction
        self.model.user_movie_matrix = user_movie_matrix
        return self.model

    def recomend_movies(self, user_id, num_recomendations=2):
        user_predictions = self.model.df_predictions.loc[user_id].sort_values(
            ascending=False)

        not_rated_movies = self.model.user_movie_matrix.loc[user_id][
            self.model.user_movie_matrix.loc[user_id] == 0].index
        recomended = user_predictions[not_rated_movies].head(
            num_recomendations)

        return recomended


RecomendationModel = RecomendationSystem()
