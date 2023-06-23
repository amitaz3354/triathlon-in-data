from typing import List


def make_athlete_yearly_racing_report(racing_year: int, data: List):
    updated_list = []
    for d in data:
        as_list = d.replace("\n", ",").replace('\t', ",").split(",")
        bla = [value for value in as_list if value != '']
        updated_list.append(bla)

    rows = updated_list.pop(0)

    results_list = []

    for data in updated_list:
        race_dict = {
            rows[0]: data[0],
            rows[1]: data[1],
            rows[2]: data[2],
            rows[3]: data[3],
            rows[4]: data[4],
            rows[5]: data[5],
            rows[6]: data[6]
        }

        results_list.append(race_dict)

    raw_data = {"races": {"year": racing_year, "results_list": results_list}}
    pto_races = extract_pto_races(raw_data)
    middle_distance_races = extract_middle_distance_races(raw_data)
    ironmans = extract_long_distance_races(raw_data)

    return [{"pto_races": pto_races}, {"middle_distance_races": middle_distance_races},
            {"long_distance_races": ironmans}]


def extract_pto_races(json_data):
    races = json_data["races"]
    pto_races = []
    res_list = races["results_list"]
    for race in res_list:
        if "PTO" in race["Race"] or "Collins" in race["Race"]:
            pto_races.append(race)

    return pto_races


def extract_middle_distance_races(json_data):
    races = json_data["races"]
    pto_races = []
    res_list = races["results_list"]
    for race in res_list:
        if "Ironman 70.3" in race["Race"] or "Challenge" in race["Race"]:
            if "Challenge Roth" in race["Race"]:
                continue
            else:
                pto_races.append(race)


    return pto_races


def extract_long_distance_races(json_data):
    races = json_data["races"]
    pto_races = []
    res_list = races["results_list"]
    for race in res_list:
        if "Ironman" in race["Race"] or "Challenge Roth" in race["Race"]:
            if "Ironman 70.3" in race["Race"]:
                continue
            else:
                pto_races.append(race)


    return pto_races
