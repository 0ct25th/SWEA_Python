from collections import deque

INF = 10000

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(r, c):
    return -1 < r < n and -1 < c < n

def bfs(sr, sc):
    dq = deque()
    dist = [[INF] * n for _ in range(n)]

    dq.append((sr, sc))
    dist[sr][sc] = adj[sr][sc]

    while len(dq):
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 유효범위 내에 있으며 방문하지 않아야 함
            if is_valid_coord(nr, nc) and dist[nr][nc] > dist[r][c] + adj[nr][nc]:
                dist[nr][nc] = dist[r][c] + adj[nr][nc]
                dq.append((nr, nc))

    return dist[n-1][n-1]



for t in range(int(input())):
    n = int(input())
    adj = [list(map(int, input())) for _ in range(n)]

    result = bfs(0, 0)
    print(f"#{t + 1} {result}")

'''
import heapq

INF = 10000

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(r, c):
    return -1 < r < n and -1 < c < n

def dijkstra(sr, sc):
    q = []
    dist = [[INF] * n for _ in range(n)]

    dist[sr][sc] = adj[sr][sc]
    heapq.heappush(q, (dist[sr][sc], sr, sc))

    while len(q):
        dt, now_r, now_c = heapq.heappop(q)

        if dist[now_r][now_c] < dt:
            continue

        for connect in graph[now_r][now_c]:
            cost = dt + connect[1]
            if cost < dist[connect[0][0]][connect[0][1]]:
                dist[connect[0][0]][connect[0][1]] = cost
                heapq.heappush(q, (cost, connect[0][0], connect[0][1]))


    return dist[n-1][n-1]



for t in range(int(input())):
    n = int(input())
    adj = [list(map(int, input())) for _ in range(n)]

    graph = [[[] for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            r, c = i, j

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid_coord(nr, nc):
                    graph[i][j].append([(nr, nc), adj[nr][nc]])


    result = dijkstra(0, 0)
    print(f"#{t + 1} {result}")
'''