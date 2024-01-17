n = int(input())
q = {
    "I": 0,
    "II": 0,
    "III": 0,
    "IV": 0
}
for _ in range(n):
    x, y = (int(i) for i in input().split())
    if not x or not y:
        print((x, y))
    else:
        if x > 0 and y > 0:
            q["I"] += 1
        elif x < 0 and y > 0:
            q["II"] += 1
        elif x < 0 and y < 0:
            q["III"] += 1
        elif x > 0 and y < 0:
            q["IV"] += 1
print(", ".join([f"{k}: {q[k]}" for k in q]) + ".")