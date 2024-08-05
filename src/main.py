from contextlib import asynccontextmanager
import json
import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse


from .constants import (
    JSON_FILE_PATH,
    ValidKind,
    ValidOrder,
)
from .data_classes import Movie
from .model import (
    get_by_actor,
    get_by_popularity,
    get_by_movies,
    get_by_similar,
)


logger = logging.getLogger(__name__)
context = {}

def load_movies():
    try:
        file_content = open(JSON_FILE_PATH, "r")
        json_database = json.load(file_content)
    except FileNotFoundError:
        logger.error("movies file is not found")
        exit(3)
    try:
        return [Movie(**movie).__dict__ for movie in json_database]
    except TypeError:
        logger.error("movies data type is triggering an error, please check the file")


# preload movies file just once when app is starting
@asynccontextmanager
async def lifespan(app: FastAPI):
    context["movies"] = load_movies
    yield
    context.clear()

app = FastAPI(lifespan=lifespan)


@app.get("/get_by/{kind}")
async def get_movies_by(
    kind: ValidKind,
    order: ValidOrder = ValidOrder.asc,
    actor_name: str = "",
    movie_name: str = "",
):
    movies = context["movies"]()
    if kind is ValidKind.popularity:
        return await get_by_popularity(movies, order)
    elif kind in [ValidKind.year, ValidKind.duration]:
        return await get_by_movies(kind.value, movies, order)
    elif kind is ValidKind.actor:
        if actor_name:
            return await get_by_actor(movies, actor_name)
        else:
            return JSONResponse(
                status_code=400,
                content={"error": "actor_name is mandatory if you get by actor"}
            )
    elif kind is ValidKind.similar:
        if movie_name:
            return await get_by_similar(movies, movie_name)
        else:
            return JSONResponse(
                status_code=400,
                content={"error": "movie_name is mandatory if you get by similar"}
            )