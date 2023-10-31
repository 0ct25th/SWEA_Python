from collections import deque


def is_valid_coord(r, c):
    return -1 < r < n and -1 < c < n


def search(sr, sc):
    cnt = adj[sr][sc]
    for i in range(2):
        nr = sr + dr[i]
        nc = sc + dc[i]
        if is_valid_coord(nr, nc):
            cnt += adj[nr][nc]
    adj[sr][sc] = cnt
    return cnt


for t in range(int(input())):
    n = int(input())

    adj = [[0] * n for _ in range(n)]
    # 위, 왼쪽 위 탐색
    dr = [-1, -1]
    dc = [0, -1]

    adj[0][0] = 1
    print(f"#{t+1}")
    for i in range(n):
        result = []
        for j in range(i + 1):
            result.append(search(i, j))
        print(*result)
