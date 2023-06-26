from typing import List

from pydantic import BaseModel


class Rankings(BaseModel):
    ...


class AthleteRank(BaseModel):
    rank: int
    athlete_name: str


class PTORankings(BaseModel):
    data: List[AthleteRank]
