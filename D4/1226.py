from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(r, c):
    return -1 < r < 16 and -1 < c < 16

def bfs(sr, sc):
    global chk
    dq = deque()
    dq.append((sr, sc))
    Visited[sr][sc] = True

    while len(dq):
        r, c = dq.popleft()

        if adj[r][c] == '3':
            chk = True
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_valid_coord(nr, nc) and not Visited[nr][nc] and adj[nr][nc] != '1':
                Visited[nr][nc] = True
                dq.append((nr, nc))


    return False



for _ in range(10):
    t = int(input())
    # 한 문자열로 입력
    adj = [list(input()) for _ in range(16)]
    sr, sc = 0, 0
    for i in range(16):
        for j in range(16):
            if adj[i][j] == '2':
                sr, sc = i, j
                break

    chk = False
    Visited = [[False] * 16 for _ in range(16)]
    bfs(sr, sc)

    if chk:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")


