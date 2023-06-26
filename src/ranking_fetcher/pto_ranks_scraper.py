import re
from typing import List

from playwright.async_api import Playwright


async def scrape_pto_ranks(playwright: Playwright, gender: str) -> List[str]:
    print("here")
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto(f"https://stats.protriathletes.org/rankings/{gender}")
    bla = await page.query_selector('.rankings')
    bla_text = await bla.text_content()
    bla2 = bla_text.replace("RankDiff.AthletePoints1", "")
    names = re.findall('[A-Za-z]+\s[A-Za-z]+', bla2)

    top_100 = []
    for i, name in enumerate(names):
        converted_name = name.lower().replace(" ", "-")
        top_100.append({"rank": i+1, "athlete_name": converted_name})

    print(top_100)

    await browser.close()

    return top_100
