from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(r, c):
    return  -1 < r < n and -1 < c < n

def bfs(sr, sc):
    dq = deque()
    dist = []

    Visited[sr][sc] = True
    dist.append(adj[sr][sc])
    dq.append((sr, sc))

    while len(dq):
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_valid_coord(nr, nc) and not Visited[nr][nc] and (abs(adj[nr][nc] - adj[r][c]) == 1):
                Visited[nr][nc] = True
                dist.append(adj[nr][nc])
                dq.append((nr, nc))

    return min(dist), len(dist)


for t in range(int(input())):
    n = int(input())
    adj = [list(map(int, input().split())) for _ in range(n)]
    Visited = [[False] * n for _ in range(n)]

    st, cnt = 1e9, 0
    for i in range(n):
        for j in range(n):
            if not Visited[i][j]:
                tmp_st, tmp_cnt = bfs(i, j)
                if cnt < tmp_cnt:
                    cnt = tmp_cnt
                    st = tmp_st
                elif cnt == tmp_cnt:
                    st = min(st, tmp_st)

    print(f"#{t+1} {st} {cnt}")