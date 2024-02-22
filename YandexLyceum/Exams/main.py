import sys
import csv
SURNAME = "Фамилия"
NAME = "имя"
RESULTS_1 = "результат 1"
RESULTS_2 = "результат 2"
RESULTS_3 = "результат 3"
RESULTS = "сумма"
n, m = (int(x) for x in input().split())
students = sys.stdin.readlines()
csv_file = open("exam.csv", mode="w", newline='')
csv_writer = csv.DictWriter(
    csv_file,
    delimiter=";",
    quotechar='"',
    fieldnames=[SURNAME, NAME, RESULTS_1, RESULTS_2, RESULTS_3, RESULTS]
)
csv_writer.writeheader()
for student in students:
    surname, name, *str_n = student.split()
    n1, n2, n3 = (int(x) for x in str_n)
    if any([n1 < m, n2 < m, n3 < m]):
        continue
    if n1 + n2 + n3 < n:
        continue
    row = [surname, name, n1, n2, n3]
    csv_writer.writerow(rowdict={
        SURNAME: surname,
        NAME: name,
        RESULTS_1: n1,
        RESULTS_2: n2,
        RESULTS_3: n3,
        RESULTS: n1 + n2 + n3
    })
csv_file.close()
