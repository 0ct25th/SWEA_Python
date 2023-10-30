for t in range(int(input())):
    n = int(input())
    stone = list(map(int, input().split()))
    min_value = abs(0 - stone[0])
    cnt = 1

    for i in range(1, n):
        if min_value == stone[i]:
            cnt += 1

        min_value = min(min_value, abs(0 - stone[i]))

    print(f"#{t+1} {min_value} {cnt}")
