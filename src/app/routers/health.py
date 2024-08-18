from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])


class Movie(BaseModel):
    name: str


@router.get("/")
def read_root():
    return "Ok"

# tests


@router.put("/movie")
def put_item(movie: Movie):
    print(movie)


@router.post("/movie")
def post_item(movie: Movie):
    print("movie received: ", movie)

# ping


@router.get("/ping")
async def ping():
    await print_pong()
    return "Ok"


async def print_pong():
    time.sleep(5)
    # asyncio.sleep(5)
    print("awake!")
