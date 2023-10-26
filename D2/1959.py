for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        a, b = b, a
        n, m = m, n

    result = []
    cnt = 0
    while cnt + n - 1 < m:
        tmp = 0
        for i in range(n):
            tmp += a[i] * b[cnt + i]
        result.append(tmp)
        cnt += 1
    print(f"#{t+1} {max(result)}")
