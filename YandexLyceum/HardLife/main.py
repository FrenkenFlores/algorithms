import csv

start, end = input().split()
rows = []
with open('journey.csv') as f:
    file = csv.reader(f, delimiter=";")
    for row in file:
        if row[0].startswith('id'):
            continue
        if int(start) <= int(row[-1]) <= int(end):
            rows.append(row)
for row in rows:
    print(f"{row[1]} ({row[2]})")
