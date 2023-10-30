for t in range(int(input())):
    h1, m1, h2, m2 = map(int, input().split())

    result_h = h1 + h2
    result_m = m1 + m2

    if result_m // 60:
        result_m %= 60
        result_h += 1

    if result_h > 12:
        result_h -= 12

    print(f"#{t+1} {result_h} {result_m}")
