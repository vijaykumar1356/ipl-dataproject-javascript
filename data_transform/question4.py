import csv
import json


def solution():
    """
    this function creates IPL's season wise matches played by each team in
    dictionary format, and total number of unique teams participated sorted in
    alphabetical manner and process the season wise data and create a new list
    of matches played by each team per season as a sublist in a parent list
    sorted according to team names sorted alphabetically.
    """
    with open('./matches.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        season_wise = {}
        # creates a season as key and
        # a dictionary of matches played by each team in a season as value
        unique_teams = {}   # creates set of unique teams for all seasons
        # with value as empty list
        for line in csv_reader:
            season_wise.setdefault(line['season'], {})
            teams = [line['team1'], line['team2']]
            for team in teams:
                season_wise[line['season']].setdefault(team, 0)
                season_wise[line['season']][team] += 1
                if team not in unique_teams:
                    unique_teams.setdefault(team, [])
        
    sort_season = dict(sorted(season_wise.items(), key=lambda x: x[0])) # sort by season year->ascending
    sort_unq_teams = dict(sorted(unique_teams.items(), key=lambda x: x[0])) # sort by alphabetical order

    for key in sort_season:
        sort_season[key] = dict(sorted(
                                    sort_season[key].items(),
                                    key=lambda x: x[0],
                                    ))
        for team in sort_unq_teams:
            if team in sort_season[key].keys():
                sort_unq_teams[team] += [sort_season[key][team]]
            else:
                sort_unq_teams[team] += [0]
    try: # for rectifying a team name duplicate in csv file
        l1 = sort_unq_teams['Rising Pune Supergiant']
        l2 = sort_unq_teams['Rising Pune Supergiants']
        del sort_unq_teams['Rising Pune Supergiant']
        final = [sum(i) for i in zip(l1, l2)]
        sort_unq_teams['Rising Pune Supergiants'] = final
    except Exception as e:
        print(e)

    season_data = []
    for i in range(len(sort_unq_teams['Rising Pune Supergiants'])):
        sub_list = []
        for key in sort_unq_teams.keys():
            sub_list.append(sort_unq_teams[key][i])
        season_data.append(sub_list)
    
    json_obj = {
        "teams": list(sort_unq_teams.keys()),
        "seasonData": season_data
    }
    with open('./all_seasons.json', 'w') as file:
        json.dump(json_obj, file, indent=2)


if __name__ == '__main__':
    solution()
