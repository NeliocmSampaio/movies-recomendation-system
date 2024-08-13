import uvicorn

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import time
import asyncio

app = FastAPI()

class Movie(BaseModel):
    name: str

@app.get("/health")
def read_root():
    return "Ok"

@app.put("/movie")
def put_item(movie: Movie):
    print(movie)

@app.post("/movie")
def post_item(movie: Movie):
    print("movie received: ", movie)

# ping

@app.get("/ping")
async def ping():
    await print_pong()
    return "Ok"

async def print_pong():
    time.sleep(5)
    # asyncio.sleep(5)
    print("awake!")

if __name__ == "__main__":
    print("main(): ...")
    uvicorn.run(app, host="127.0.0.1", port=8080)