import json
import csv


json_list = []
with open("people.csv") as f:
    reader = csv.reader(f, delimiter="_")
    headers = {k: i for i, k in enumerate(reader.__next__())}
    for i in reader:
        if not len(set(i[headers["event"]].split()) & set(i[headers["explanation"]].split())) \
                and i[headers["benefit"]] != 0:
            out = {
                "name": i[headers["name"]],
                "event": i[headers["event"]],
                "benefit": i[headers["benefit"]]
            }
            json_list.append(out)
if len(json_list):
    with open("dubious.json", 'w') as f:
        json.dump(json_list, f, indent=4)
