import csv
import json


def main():
    evil = {}
    evil_list = []
    with open("fears.csv") as file:
        csv_reader = csv.reader(file)
        rows = [row for row in csv_reader]
        for row in rows[1:]:
            world = row[1]
            danger = row[2]
            level = row[3]
            if int(level) <= 5:
                continue
            if world in evil:
                evil[world] = "; ".join([evil.get(world), danger])
            else:
                evil[world] = danger
        for e in evil:
            evil_list.append({
                "world": e,
                "dangers": evil[e]
            })
    with open('evil.csv', 'w') as csvf:
        json.dump(fp=csvf, obj=evil_list, indent=4)
