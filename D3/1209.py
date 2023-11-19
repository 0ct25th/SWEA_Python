from collections import deque

def is_valid_coord(r, c):
    return -1 < r < N and -1 < c < N

def r_bfs(sr, sc):
    global r_crs

    dq = deque()
    dq.append((sr, sc))
    r_crs += arr[sr][sc]

    while dq:
        r, c = dq.popleft()

        nr, nc = r + 1, c + 1
        if is_valid_coord(nr, nc):
            r_crs += arr[nr][nc]
            dq.append((nr, nc))


def l_bfs(sr, sc):
    global l_crs

    dq = deque()
    dq.append((sr, sc))
    l_crs += arr[sr][sc]

    while dq:
        r, c = dq.popleft()

        nr, nc = r + 1, c - 1
        if is_valid_coord(nr, nc):
            l_crs += arr[nr][nc]
            dq.append((nr, nc))


for _ in range(10):
    t = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    row_max, col_max, l_crs, r_crs = -1e9, -1e9, 0, 0

    for i in range(N):
        # 행마다 합 구하기
        row_max = max(row_max, sum(arr[i]))

        tmp = 0
        # 열마다 합 구하기
        for j in range(N):
            tmp += arr[j][i]
        col_max = max(col_max, tmp)

    # 오른쪽 대각선 합 구하기
    r_bfs(0, 0)
    # 왼쪽 대각선 합 구하기
    l_bfs(0, N - 1)

    result = max(max(row_max, col_max), max(l_crs, r_crs))
    print(f"#{t} {result}")


