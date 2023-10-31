from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid_coord(sr, sc, r, c):
    return sr - 1 < r < sr + 3 and sc - 1 < c < sc + 3


def bfs(sr, sc):
    global chk
    dq = deque()
    dq.append((sr, sc))
    # 좌표 방문 여부 체크
    Visited[sr][sc] = True
    # 1~9까지 숫자가 이미 나왔는지 체크
    Visited_num = [False] * 10
    Visited_num[board[sr][sc]] = True

    while len(dq):
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_valid_coord(sr, sc, nr, nc) and not Visited[nr][nc]:
                if not Visited_num[board[nr][nc]]:
                    Visited[nr][nc] = True
                    Visited_num[board[nr][nc]] = True
                    dq.append((nr, nc))
                else:
                    chk = False
                    return


for t in range(int(input())):
    chk = True
    board = [list(map(int, input().split())) for _ in range(9)]
    Visited = [[False] * 9 for _ in range(9)]

    # 행렬 겹치는 문자 있는지확인
    for i in range(9):
        row_nums = [False] * 10
        col_nums = [False] * 10
        for j in range(9):
            if not row_nums[board[j][i]] and not col_nums[board[i][j]]:
                row_nums[board[j][i]] = True
                col_nums[board[i][j]] = True
            else:
                chk = False
                break

    # 3*3 겹치는 문자 있는지 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bfs(i, j)

        if chk:
            continue
        else:
            break

    if chk:
        print(f"#{t+1} 1")
    else:
        print(f"#{t+1} 0")
