for _ in range(10):
    t = int(input())
    adj = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if adj[99][i] == 2:
            c = i

    r = 99
    while r > 0:
        r -= 1  # 항상 위로 가므로 r은 1 감소
        if 0 < c and adj[r][c - 1] == 1:  # 왼쪽으로 가는 경우
            while 0 < c and adj[r][c - 1] == 1:
                c -= 1
        elif c < 99 and adj[r][c + 1] == 1:  # 오른쪽으로 가는 경우
            while c < 99 and adj[r][c + 1] == 1:
                c += 1

    print(f"#{t} {c}")
