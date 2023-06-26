from typing import Callable, Any

from playwright.async_api import async_playwright

from src.ranking_fetcher.pto_ranks_scraper import scrape_pto_ranks
from src.shared.dto.ranking_fetcher.rankings import PTORankings


class RankingFetcherService:

    async def fetch_pto_ranks_man(self):
        data = await self.__scrape_something(scrape_pto_ranks, gender="man")
        print(data)
        return PTORankings(data=data)

    async def fetch_pto_ranks_woman(self):
        data = await self.__scrape_something(scrape_pto_ranks, gender="women")
        return PTORankings(data=data)

    async def __scrape_something(self, scraping_func: Callable, *args, **kwargs) -> Any:
        async with async_playwright() as playwright:
            res = await scraping_func(playwright, *args, **kwargs)
            return res
