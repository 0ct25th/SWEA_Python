from collections import deque

pipe = [[0, 0, 0, 0], # 0번 파이프
        [1, 1, 1, 1],   # 1번
        [1, 1, 0, 0],   # 2번
        [0, 0, 1, 1],   # 3번
        [1, 0, 0, 1],   # 4번
        [0, 1, 0, 1],   # 5번
        [0, 1, 1, 0],   # 6빈
        [1, 0, 1, 0]]   # 7번

# 반대 방향 체크
opp = [1, 0, 3, 2]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(r, c):
    return -1 < r < N and -1 < c < M

def bfs(sr, sc):
    dq = deque()
    dist = [[0] * M for _ in range(N)]
    cnt = 0

    dq.append((sr, sc))
    dist[sr][sc] = 1
    cnt += 1

    while len(dq):
        r, c = dq.popleft()

        if dist[r][c] == L:
            return cnt

        # 4방향, 범위 내, 중복 불허용, 조건 확인(현 위치 - 이동 위치 파이프 존재)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_valid_coord(nr, nc) and dist[nr][nc] == 0 and pipe[adj[r][c]][i] == 1 and pipe[adj[nr][nc]][opp[i]] == 1:
                    cnt += 1
                    dist[nr][nc] = dist[r][c] + 1
                    dq.append((nr,nc))

    return cnt

for t in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(N)]


    result = bfs(R, C)
    print(f"#{t+1} {result}")