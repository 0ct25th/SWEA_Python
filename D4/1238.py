import heapq

INF = 987654321

def dijkstra(st):
    q = []
    heapq.heappush(q, (0, st))
    dist = [INF] * 100
    # 시작 노드 값 0으로 초기화
    dist[st] = 0

    while len(q):
        dt, now = heapq.heappop(q)

        if dist[now] < dt:
            continue

        for connect in graph[now]:
            cost = dt + connect[1]
            if cost < dist[connect[0]]:
                dist[connect[0]] = cost
                heapq.heappush(q, (cost, connect[0]))

    return dist


for t in range(10):
    # 데이터 길이, 시작점 입력
    n, st = map(int, input().split())
    string = list(map(int, input().split()))
    # [i]: 대상 노드
    # [i][0]: 연결 노드
    # [i][1]: 거리
    graph = [[] for _ in range(100)]
    for i in range(0, n, 2):
        a, b = string[i], string[i + 1]
        graph[a - 1].append((b - 1, 1))

    receive = dijkstra(st - 1)
    max_call = -1e9
    result = 0
    for i in range(100):
        if receive[i] == INF:
            continue
        else:
            if max_call <= receive[i]:
                max_call = receive[i]
                result = i + 1
    print(f"#{t + 1} {result}")
