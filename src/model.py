from typing import List

from .constants import (
    RATING_SIMILAR_VALUE,
    SIMILAR_QUANTITY,
)


async def get_by_popularity(movies: List[dict], order: str = "asc"):
    return sorted(movies, key=lambda x: (x["rating_average"], x["viewerCount"]), reverse=order=="desc")


async def get_by_movies(kind: str, movies: List[dict], order: str = "asc"):
    key = "year" if kind == "year" else "duration_in_minutes"
    return sorted(movies, key=lambda x: (x[key]), reverse=order=="desc")


async def get_by_actor(movies: List[dict], actor_name: str):
    return list(filter(lambda x: actor_name in x["actors"], movies))


async def get_by_similar(movies: List[dict], movie_name: str):
    movie_initial = list(filter( lambda x: movie_name == x["title"], movies))
    movies_by_gender = []
    movies_by_rating = []
    movies_by_cast = []
    if len(movie_initial) == 1:
        movie_initial = movie_initial[0]
        for movie in movies:
            if movie_initial["title"] != movie["title"]:
                intersection_gender = set(movie["genres"]).intersection(set(movie_initial["genres"]))
                if len(intersection_gender)==len(movie_initial["genres"]):
                    movies_by_gender.append(movie)
                if (
                    (movie["rating_average"] - RATING_SIMILAR_VALUE)  < movie_initial["rating_average"] and
                    (movie_initial["rating_average"] < movie["rating_average"] + RATING_SIMILAR_VALUE)
                ):
                    movies_by_rating.append(movie)
                intersection_cast = set(movie["actors"]).intersection(set(movie_initial["actors"]))
                if len(intersection_cast)==len(movie_initial["genres"]):
                    movies_by_cast.append(movie)
        if len(movies_by_gender) > SIMILAR_QUANTITY:
            return movies_by_gender[0:20]
        else:
            set_by_gender = set(movies_by_gender)
            set_by_rating = set(movies_by_rating)
            gender_and_rating = list(set_by_gender.union(set_by_rating))
            if len(gender_and_rating) > SIMILAR_QUANTITY:
                return gender_and_rating[0:20]
            else:
                set_by_gender_and_rating = set(gender_and_rating)
                set_by_cast = set(movies_by_cast)
                gender_and_rating_and_cast = list(set_by_gender_and_rating.union(set_by_cast))
                return gender_and_rating_and_cast[0:20]

    else:
        return {"error": "movie doesn't found, please check movie name"}