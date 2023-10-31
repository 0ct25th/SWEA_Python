for t in range(int(input())):
    n = int(input())

    result = [0] * 8
    if n >= 50000:
        result[0] = n // 50000
        n %= 50000

    if n >= 10000:
        result[1] = n // 10000
        n %= 10000

    if n >= 5000:
        result[2] = n // 5000
        n %= 5000

    if n >= 1000:
        result[3] = n // 1000
        n %= 1000

    if n >= 500:
        result[4] = n // 500
        n %= 500

    if n >= 100:
        result[5] = n // 100
        n %= 100

    if n >= 50:
        result[6] = n // 50
        n %= 50

    if n >= 10:
        result[7] = n // 10
        n %= 10

    print(f"#{t+1}")
    print(*result)
