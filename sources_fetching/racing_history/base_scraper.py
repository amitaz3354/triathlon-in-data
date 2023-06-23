from playwright.sync_api import Playwright, sync_playwright

from sources_fetching.racing_history.mongo_client import import_athlete
from sources_fetching.racing_history.table_to_json import make_athlete_yearly_racing_report
from sources_fetching.racing_history.top_men import top_100_men


def run(playwright: Playwright, name: str) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"https://stats.protriathletes.org/athlete/{name}")
    page.wait_for_load_state()
    page.get_by_role("button", name="Allow all").click()

    nth_to_year = {
        0: 2023,
        1: 2022,
        2: 2021
    }

    l = []

    for i in range (3):
        results = page.get_by_role(f"table >> nth={i}").get_by_role("row").all_inner_texts()
        res = make_athlete_yearly_racing_report(racing_year=nth_to_year.get(i), data=results)
        l.append({"year": nth_to_year.get(i), "results": res})

    res = {
     "name":name,
     "race_results": l
    }

    print(res)

    import_athlete(res)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    for name in top_100_men:
        run(playwright, name)
