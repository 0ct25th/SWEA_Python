def is_valid_coord(r, c):
    return -1 < r < n and -1 < c < n

def np():
    # 모든 좌표 순회
    for i in range(n):
        for j in range(n):
            # 열(오른쪽), 행(아래쪽), 대각선(오른쪽\, 왼쪽/) 순으로 확인
            for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                # 선택한방향으로 5개 돌을 순회
                for k in range(5):
                    nr = i + dr * k
                    nc = j + dc * k
                    if is_valid_coord(nr, nc) and adj[nr][nc] == 'o':
                        # 돌이 있으면 계속 순회
                        pass
                    else:
                        # 돌이 없으면 순회 중단
                        break
                # break(돌이 없지 않으면)안하고 수행되면 YES 반환
                else:
                    return "YES"
    # 멈추지 않고 계속 순회했다면 5개 연속된 돌을 찾지 못한 것이므로 NO 반환
    return "NO"


for t in range(int(input())):
    n = int(input())
    adj = [list(input()) for _ in range(n)]

    result = np()
    print(f"#{t+1} {result}")