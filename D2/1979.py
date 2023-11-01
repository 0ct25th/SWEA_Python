from collections import deque
import sys

input = sys.stdin.readline


def is_valid_coord(r, c):
    return -1 < r < n and -1 < c < n


def r_bfs(sr, sc):
    dq = deque()
    r_Visited[sr][sc] = True
    dq.append((sr, sc))
    cnt = 1

    while len(dq):
        r, c = dq.popleft()

        nr, nc = r + 1, c
        if is_valid_coord(nr, nc) and not r_Visited[nr][nc] and board[nr][nc] == 1:
            cnt += 1
            r_Visited[nr][nc] = True
            dq.append((nr, nc))

    return cnt


def c_bfs(sr, sc):
    dq = deque()
    c_Visited[sr][sc] = True
    dq.append((sr, sc))
    cnt = 1

    while len(dq):
        r, c = dq.popleft()

        nr, nc = r, c + 1
        if is_valid_coord(nr, nc) and not c_Visited[nr][nc] and board[nr][nc] == 1:
            cnt += 1
            c_Visited[nr][nc] = True
            dq.append((nr, nc))

    return cnt


for t in range(int(input())):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    r_Visited = [[False] * n for _ in range(n)]
    c_Visited = [[False] * n for _ in range(n)]

    result = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and (not r_Visited[i][j] or not c_Visited[i][j]):
                result.append(r_bfs(i, j))
                result.append(c_bfs(i, j))

    print(f"#{t+1} {result.count(k)}")
