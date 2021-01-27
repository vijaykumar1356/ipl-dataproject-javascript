import csv
import json


def solution():
    """
    this function creates a dictionary of rcb_batsmen names and runs scored
    from all seasons and sort them in ascending order of scores and send the
    data to plot a bar chart of TOP batsmen of RCB with runs.
    """
    with open("./deliveries_new.csv", 'r') as csv_file:
        rcb_batsmen_scores = {}
        file_reader = csv.DictReader(csv_file)
        for row in file_reader:
            if row['batting_team'] == 'Royal Challengers Bangalore':
                rcb_batsmen_scores.setdefault(row['batsman'], 0)
                rcb_batsmen_scores[row['batsman']] += int(row['batsman_runs'])

    sort_batsmen_scores = dict(sorted(
                                rcb_batsmen_scores.items(),
                                key=lambda x: x[1],
                                reverse=True))
    json_obj = {
        "batsmen": list(sort_batsmen_scores.keys())[:15],
        "total_score": list(sort_batsmen_scores.values())[:15],
    }
    with open("./rcb_batsmen_runs.json", 'w') as f:
        json.dump(json_obj, f, indent=2)


if __name__ == '__main__':
    solution()
