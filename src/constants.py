from enum import Enum


JSON_FILE_PATH = "./data/movies.json"

RATING_SIMILAR_VALUE = 0.2
SIMILAR_QUANTITY = 20

class ValidKind(str, Enum):
    popularity = "popularity"
    similar = "similar"
    actor = "actor"
    duration = "duration"
    year = "year"

class ValidOrder(str, Enum):
    asc = "asc"
    desc = "desc"