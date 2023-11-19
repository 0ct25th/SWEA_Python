def dfs(node, cnt):
    global result
    result = max(result, cnt)

    Visited[node] = True

    for i in range(N):
        if not Visited[i] and i in graph[node]:
            dfs(i, cnt + 1)
            Visited[i] = False

for t in range(int(input())):
    N, M = map(int, input().split())

    if M == 0:
        print(f"#{t + 1} {1}")

    graph = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    result = 0
    for i in range(N):
        Visited = [False] * N
        dfs(i, 1)

    print(f"#{t + 1} {result}")