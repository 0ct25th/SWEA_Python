from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid_coord(sr, sc, r, c):
    return sr - 1 < r < sr + m and sc - 1 < c < sc + m


def bfs(sr, sc):
    global cnt
    dq = deque()
    dq.append((sr, sc))
    Visited = [[False] * n for _ in range(n)]
    Visited[sr][sc] = True

    while len(dq):
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_valid_coord(sr, sc, nr, nc) and not Visited[nr][nc]:
                cnt += adj[nr][nc]
                Visited[nr][nc] = True
                dq.append((nr, nc))

    return cnt


for t in range(int(input())):
    n, m = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(n)]

    result = []
    if n != m:
        for i in range(n - m + 1):
            for j in range(n - m + 1):
                cnt = adj[i][j]
                result.append(bfs(i, j))
        print(f"#{t+1} {max(result)}")
    else:
        result = 0
        for i in range(n):
            for j in range(n):
                result += adj[i][j]
        print(f"#{t+1} {result}")
