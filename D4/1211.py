for _ in range(10):
    t = int(input())
    adj = [list(map(int, input().split())) for _ in range(100)]
    
    # 모든 출발점 찾기
    start = []
    for i in range(100):
        if adj[0][i] == 1:
            start.append(i)
            
    # 모든 출발점에서 거리 측정
    result = [1e9, 1e9]
    for i in range(len(start)):
        r, c = 0, start[i]
        tmp = 0
        while r < 100:
            if 0 < c and adj[r][c - 1] == 1:  # 왼쪽으로 가는 경우
                while 0 < c and adj[r][c - 1] == 1:
                    c -= 1
                    tmp += 1
            elif c < 99 and adj[r][c + 1] == 1:  # 오른쪽으로 가는 경우
                while c < 99 and adj[r][c + 1] == 1:
                    c += 1
                    tmp += 1
            else: # 아래쪽으로 가는 경우
                tmp += 1
            r += 1
        if tmp < result[0]:
            print(result)
            result = [tmp, start[i]]
            print(result)
    
    
    print(f"#{t} {result[1]}")