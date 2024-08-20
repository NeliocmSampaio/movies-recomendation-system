import uvicorn

from fastapi import FastAPI

from .api.controllers import movie
from .api.controllers import user
from .api.controllers import health
from .api.controllers import recomendation

from .infrastructure.db.mysql import engine, Base

from .infrastructure.db.models.user import UserModel
from .infrastructure.db.models.movie import MovieModel
from .infrastructure.db.models.artist import ArtistModel
from .infrastructure.db.models.director import DirectorModel

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(recomendation.router)
app.include_router(movie.router)
app.include_router(user.router)
app.include_router(health.router)

if __name__ == "__main__":
    print("main(): ...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
