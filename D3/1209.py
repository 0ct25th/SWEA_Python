from collections import deque


def is_valid_coord(r, c):
    return -1 < r < 100 and -1 < c < 100


# 대각선 합 구하기
def r_bfs(sr, sc):
    dq = deque()
    dq.append((sr, sc))
    right_sum = arr[sr][sc]

    while len(dq):
        r, c = dq.popleft()
        nr = r + 1
        nc = c - 1
        if is_valid_coord(nr, nc):
            right_sum += arr[nr][nc]
            dq.append((nr, nc))

    return right_sum


def l_bfs(sr, sc):
    dq = deque()
    dq.append((sr, sc))
    left_sum = arr[sr][sc]

    while len(dq):
        r, c = dq.popleft()
        nr = r + 1
        nc = c + 1
        if is_valid_coord(nr, nc):
            left_sum += arr[nr][nc]
            dq.append((nr, nc))

    return left_sum


for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row_max, col_max = -1e9, -1e9
    right_max, left_max = -1e9, -1e9
    for i in range(len(arr)):
        row_sum, col_sum = 0, 0
        # 행, 열 합 중 최대값 구하기
        for j in range(len(arr)):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        row_max = max(row_max, row_sum)
        col_max = max(col_max, col_sum)
    right_max = r_bfs(0, len(arr) - 1)
    left_max = l_bfs(0, 0)

    result = max(max(row_max, col_max), max(right_max, left_max))
    print(f"#{t} {result}")
