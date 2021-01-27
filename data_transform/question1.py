import csv
import json


def solution():
    """
    this function creates a dictionary of all the teams and their total runs
    over the history of IPL(2008-2017) and sort the data in descending order
    of runs scored and send the data as arguments to plot a bar graph.
    """
    with open("deliveries_new.csv", 'r') as csv_file:
        teams_runs = {}
        file_reader = csv.DictReader(csv_file)
        for row in file_reader:
            teams_runs.setdefault(row['batting_team'], 0)
            teams_runs[row['batting_team']] += int(row['total_runs'])

    sort_teams = dict(
                    sorted(
                        teams_runs.items(),
                        key=lambda x: x[1],
                        reverse=True))

    json_obj = {
        "teams": list(sort_teams.keys()),
        "total_runs": list(sort_teams.values())
    }
    with open("teams_scores.json", 'w') as f:
        json.dump(json_obj, f, indent=2)

if __name__ == '__main__':
    solution()
