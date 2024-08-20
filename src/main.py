import uvicorn

from fastapi import FastAPI

from .api.controllers import movie
from .api.controllers import user
from .api.controllers import health

from .infrastructure.db.mysql import engine, Base

from .infrastructure.db.models.user import User
from .infrastructure.db.models.movie import Movie
from .infrastructure.db.models.artist import Artist
from .infrastructure.db.models.director import Director

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(movie.router)
app.include_router(user.router)
app.include_router(health.router)

if __name__ == "__main__":
    print("main(): ...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
