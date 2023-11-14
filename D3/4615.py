dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def is_valid_coord(r, c):
    return -1 < r < N and -1 < c < N

def flip(sr, sc):
    # 현재 돌 색 저장
    cur = board[sr][sc]

    # 8방향 탐색
    for i in range(8):
        # 돌 변경 예정 좌표들 저장
        reverse = []
        nr, nc = sr + dr[i], sc + dc[i]

        # 조건 만족시 해당 방향으로 계속 탐색
        while is_valid_coord(nr, nc) and board[nr][nc] != 0 and board[nr][nc] != cur:
            reverse.append((nr, nc))
            nr += dr[i]
            nc += dc[i]

        # 자신의 돌을 만나면 사이에 있는 상대방의 돌을 모두 자신의 돌로 바꿈
        if is_valid_coord(nr, nc) and board[nr][nc] == cur:
            for r, c in reverse:
                board[r][c] = cur

for t in range(int(input())):
    # N: 보드 크기, M: 돌 변경 횟수
    N, M = map(int, input().split())

    # 초기 돌 배치
    board = [[0] * N for _ in range(N)]
    # 초기 흑돌 배치
    board[N//2 - 1][N//2] = board[N//2][N//2 - 1] = 'B'
    # 초기 백돌 배치
    board[N//2][N//2] = board[N//2 - 1][N//2 - 1] = 'W'

    # M만큼 돌 입력
    for _ in range(M):
        # 입력 조심
        c, r, clr = map(int, input().split())

        # 흑돌 놓기
        if clr == 1:
            board[r-1][c-1] = 'B'
        # 백돌 놓기
        else:
            board[r-1][c-1] = 'W'

        # 돌 변경
        flip(r-1, c-1)

    # 각 돌 개수 세기
    black, white = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'B':
                black += 1
            elif board[i][j] == 'W':
                white += 1

    print(f"#{t + 1} {black} {white}")
