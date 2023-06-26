from fastapi import FastAPI
from datetime import datetime

from src.ranking_fetcher.ranking_fetcher_service import RankingFetcherService

app = FastAPI(
    title="Ranking Fetcher",
    description="A service that fetches Triathlon rankings from different organizations"
)


@app.get("/ranking-fetcher/pto", status_code=200)
async def fetch_pto_rankings():
    man = await RankingFetcherService().fetch_pto_ranks_man()
    women = await RankingFetcherService().fetch_pto_ranks_woman()
    return {
        "Date": datetime.now(),
        "Man Rankings": man,
        "Women Rankings": women
    }
