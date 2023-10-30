def is_valid_coord(r, c):
    return -1 < r < n and -1 < c < n


# 우 dfs
def d_dfs():
    global r, c, cnt

    result[r][c] = cnt
    Visited[r][c] = True

    r += dr[0]
    c += dc[0]
    if is_valid_coord(r, c) and not Visited[r][c]:
        cnt += 1
        d_dfs()


# 하 dfs
def s_dfs():
    global r, c, cnt
    result[r][c] = cnt
    Visited[r][c] = True

    r += dr[1]
    c += dc[1]
    if is_valid_coord(r, c) and not Visited[r][c]:
        cnt += 1
        s_dfs()


# 좌 dfs
def a_dfs():
    global r, c, cnt
    result[r][c] = cnt
    Visited[r][c] = True

    r += dr[2]
    c += dc[2]
    if is_valid_coord(r, c) and not Visited[r][c]:
        cnt += 1
        a_dfs()


# 상
def w_dfs():
    global r, c, cnt
    result[r][c] = cnt
    Visited[r][c] = True

    r += dr[3]
    c += dc[3]
    if is_valid_coord(r, c) and not Visited[r][c]:
        cnt += 1
        w_dfs()


for t in range(int(input())):
    n = int(input())

    # 우, 하, 좌, 상 순서대로 탐색
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    Visited = [[False] * n for _ in range(n)]
    result = [[0] * n for _ in range(n)]

    cnt, r, c = 1, 0, 0
    while cnt < n * n:
        d_dfs()
        c -= 1
        s_dfs()
        r -= 1
        a_dfs()
        c += 1
        w_dfs()
        r += 1

    print(f"#{t+1}")
    if n == 1:
        print(1)
    else:
        for i in result:
            print(*i)
