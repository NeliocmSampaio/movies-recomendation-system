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

# from pyspark.ml.recommendation import ALS
# from pyspark.ml.evaluation import RegressionEvaluator


class Visualization:
    user: User
    movie: Movie


class Model:
    df_predictions: pd.DataFrame
    user_movie_matrix: pd.DataFrame


class VisualizationHistory:
    log: List[Visualization]

    def get_history(self, db: Session):
        users = db.query(UserModel).all()

        data = []
        for user in users:
            for movie in user.movies:
                rating = db.query(user_movie_association.c.rate).filter_by(
                    user_id=user.id, movie_id=movie.id).scalar()

                data.append(
                    {
                        "user_id": user.id,
                        "movie_id": movie.id,
                        "director": movie.director_id,
                        "artists": [artist.id for artist in movie.artists],
                        "rating": rating
                    }
                )

        df = pd.DataFrame(data)

        mlb_artists = MultiLabelBinarizer()
        artists_encoded = mlb_artists.fit_transform(df["artists"])

        df_artists = pd.DataFrame(
            artists_encoded, columns=mlb_artists.classes_)

        df = pd.concat([df, df_artists], axis=1)

        df.drop(columns=["artists"], inplace=True)

        return df

        # spark = SparkSession.builder.master('local[*]').getOrCreate()
        # ratings = spark.createDataFrame(df)

        # (training, test) = ratings.randomSplit([0.8, 0.2])
        # als = ALS(maxIter=5, regParam=0.01, userCol="user_id",
        #           itemCol="movie_id", ratingCol="rating", coldStartStrategy="drop")

        # model = als.fit(training)

        # predictions = model.transform(test)
        # evaluator = RegressionEvaluator(
        #     metricName="rmse", labelCol="rating", predictionCol="prediction")

        # rmse = evaluator.evaluate(predictions)
        # print("Error = ", str(rmse))

    def train_recomendation(self, df):
        print(df)

        user_movie_matrix = df.pivot_table(
            index='user_id', columns='movie_id', values='rating')
        user_movie_matrix.fillna(0, inplace=True)

        print(user_movie_matrix)

        movies_similarity = cosine_similarity(user_movie_matrix.T)
        prediction_matrix = np.dot(user_movie_matrix, movies_similarity)

        normalization_factor = np.array(
            [np.abs(movies_similarity).sum(axis=1)])
        prediction_matrix = prediction_matrix / normalization_factor

        df_prediction = pd.DataFrame(
            prediction_matrix, index=user_movie_matrix.index, columns=user_movie_matrix.columns)

        print(df_prediction)

        model = Model()
        model.df_predictions = df_prediction
        model.user_movie_matrix = user_movie_matrix
        return model

        # n_components = 20
        # svd = TruncatedSVD(n_components=n_components)
        # latent_matrix = svd.fit_transform(user_movie_matrix)
        # reconstructed_matrix = np.dot(latent_matrix, svd.components_)
        # df_reconstructed = pd.DataFrame(reconstructed_matrix, index=user_movie_matrix.index, columns=user_movie_matrix.columns)

    def recomend_movies(self, model: Model, user_id, num_recomendations=2):
        user_predictions = model.df_predictions.loc[user_id].sort_values(
            ascending=False)
        not_rated_movies = model.user_movie_matrix.loc[user_id][
            model.user_movie_matrix.loc[user_id] == 0].index
        recomended = user_predictions[not_rated_movies].head(
            num_recomendations)
        # print(recomended)
        return recomended
