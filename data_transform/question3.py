import csv
import json


def solution():
    """
    this function fetches the umpires and their nationality from a csv file
    umpires_nation.csv and evaluates the number of foreign umpires
    participated in IPL country wise and sort the data descending order of
    number.
    """
    with open('./matches.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        match_umpires = []
        for line in csv_reader:
            umpires = [line['umpire1'], line['umpire2'], ]
            for umpire in umpires:
                if umpire != "" and umpire not in match_umpires:
                    match_umpires.append(umpire)

    with open('./umpires_nation.csv', 'r') as csv_file:
        # this file has been generated with the help of scrape_umpires.py file,
        # where I used Beautiful Soup module to scrape the list of umpires and
        # their nationality.
        csv_reader = csv.DictReader(csv_file)
        name_nationality = {}
        for line in csv_reader:
            name_nationality[line['umpire']] = line['nationality']

    country_umpire = {}
    # country as key and no. of umpires belongs to that country as value
    for umpire in match_umpires:
        for person in name_nationality.keys():
            if umpire.split()[1] in person.split():
                if name_nationality[person] == 'India':
                    continue
                country_umpire.setdefault(name_nationality[person], 0)
                country_umpire[name_nationality[person]] += 1
                
    sorted_country_umpire = dict(sorted(
                                country_umpire.items(),
                                key=lambda x: x[1],
                                reverse=True))
    json_obj = {
        "countries": list(sorted_country_umpire.keys()),
        "no_of_umpires": list(sorted_country_umpire.values())
    }
    with open('./country_umpire_count.json', 'w') as f:
        json.dump(json_obj, f, indent=2)
    

if __name__ == '__main__':
    solution()
