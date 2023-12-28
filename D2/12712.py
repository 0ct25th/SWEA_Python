def is_valid_coord(coord):
    return -1 < coord < N

for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # +모양으로 더하기
    for r in range(N):
        for c in range(N):
            tmp = 0
            for m in range(M):
                # 상 방향
                if is_valid_coord(r - m):
                    tmp += arr[r - m][c]
                # 하 방향
                if is_valid_coord(r + m):
                    tmp += arr[r + m][c]
                # 좌 방향
                if is_valid_coord(c - m):
                    tmp += arr[r][c - m]
                # 우 방향
                if is_valid_coord(c + m):
                    tmp += arr[r][c + m]
            tmp -= 3 * arr[r][c]  # 중복 빼기
            result = max(result, tmp)

    # x모양으로 더하기
    for r in range(N):
        for c in range(N):
            tmp = 0
            for m in range(M):
                # 좌상 방향
                if is_valid_coord(r - m) and is_valid_coord(c - m):
                    tmp += arr[r - m][c - m]
                # 우상 방향
                if is_valid_coord(r - m) and is_valid_coord(c + m):
                    tmp += arr[r - m][c + m]
                # 좌하 방향
                if is_valid_coord(r + m) and is_valid_coord(c - m):
                    tmp += arr[r + m][c - m]
                # 우하 방향
                if is_valid_coord(r + m) and is_valid_coord(c + m):
                    tmp += arr[r + m][c + m]
            tmp -= 3 * arr[r][c]  # 중복 빼기
            result = max(result, tmp)
    print(f'#{t + 1} {result}')