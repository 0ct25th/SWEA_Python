def dfs(node, cnt):
    global result

    result = max(result, cnt)
    Visited[node] = True

    for i in range(N):
        # 방문하지 않았고 서로 연결되어 있다면
        if not Visited[i] and graph[node][i]:
            # dfs 실행
            dfs(i, cnt + 1)
            Visited[i] = False

for t in range(int(input())):
    N, M = map(int, input().split())

    graph = [[0] * N for _ in range(N)]
    Visited = [False] * N

    # 그래프 정점 연결
    for _ in range(M):
        # 연결된 두 정점
        x, y = map(int, input().split())
        graph[x-1][y-1] = graph[y-1][x-1] = 1

    result = 0
    for i in range(N):
        dfs(i, 1)
        Visited[i] = False

    print(f"#{t+1} {result}")
