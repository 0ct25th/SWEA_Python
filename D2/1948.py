month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

for t in range(int(input())):
    m1, d1, m2, d2 = map(int, input().split())

    if m2 - m1 == 0:
        print(f"#{t+1} {d2 - d1 + 1}")
    else:
        day = -d1 + d2
        for i in range(m1, m2):
            day += month[i]
        print(f"#{t+1} {day + 1}")
