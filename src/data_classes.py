from dataclasses import dataclass, field
from typing import List


@dataclass
class Movie:
    title: str
    year: int
    genres: List[str]
    ratings: List[int]
    viewerCount: int
    storyline: str
    actors: List[str]
    duration: str
    releaseDate: str
    contentRating: str
    posterImage: str
    rating_average: float = field(init=False)
    duration_in_minutes: int = field(init=False)

    def __post_init__(self):
        self.rating_average = sum(self.ratings) / len(self.ratings)
        self.duration_in_minutes = int(self.duration.replace("PT", "").replace("M", ""))

    