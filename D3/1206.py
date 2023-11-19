from collections import deque

for t in range(10):
    # 건물 개수 입력
    N = int(input())
    # 건물 높이 입력
    building = deque(map(int, input().split()))
    # 건물 앞, 뒤 2개씩 0으로 설정
    for i in range(2):
        building.appendleft(0)
        building.append(0)

    result = 0
    # 건물 차이 확인
    for i in range(2, N):
        max_high = max(max(building[i-2:i]), max(building[i+1:i+3]))
        if building[i] - max_high > 0:
            result += building[i] - max_high

    print(f"#{t + 1} {result}")