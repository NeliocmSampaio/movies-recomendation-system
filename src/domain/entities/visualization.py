from .user import User
from .artist import Artist
from .director import Director
from .movie import Movie
from sqlalchemy.orm import Session
from typing import List
from ...infrastructure.db.models.user import UserModel
from ...infrastructure.db.models.movie import MovieModel


class Visualization:
    user: User
    movie: Movie


class VisualizationHistory:
    log: List[Visualization]

    def get_history(self, db: Session):
        users = db.query(UserModel).all()

        data = []
        for user in users:
            user_data = [user.id]
            for movie in user.movies:
                print(movie.name)
                user_data.append(movie.id)
                user_data.append(movie.directors.id)
                for artist in movie.artists:
                    user_data.append(artist.id)

        print(data)
