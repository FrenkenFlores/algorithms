import csv
PLACE = "place"
USER_NAME = "user_name"
LOGIN = "login"
SCORE_1 = "1(Система счисления)"
SCORE_2 = "2(Количество символов)"
SCORE_3 = "3(Минимальное число)"
SCORE_4 = "4(Трамвай)"
SCORE = "Score"
school_number, class_number = input().split(' ')
users = []
with open(file="rez.csv", mode='r') as f:
    reader = csv.DictReader(f=f)
    for row in reader:
        if f"{int(school_number):02} {int(class_number):02}" in row[USER_NAME]:
            users.append({row[USER_NAME].split()[3]: row[SCORE]})
users = sorted(users, key=lambda d: str(*list(d.keys())), reverse=True)
users = sorted(users, key=lambda d: int(*list(d.values())), reverse=True)
for user in users:
    print(f"{str(*user.keys())} {str(*user.values())}")