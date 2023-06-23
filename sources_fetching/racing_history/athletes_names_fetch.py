import re
from playwright.sync_api import Playwright, sync_playwright

# todo fix script with names
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://stats.protriathletes.org/rankings/men")
    bla = page.query_selector('.rankings').text_content()
    bla2 = bla.replace("RankDiff.AthletePoints1", "")
    names = re.findall('[A-Za-z]+\s[A-Za-z]+', bla2)
    print(names)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
