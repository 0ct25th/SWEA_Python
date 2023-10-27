for t in range(int(input())):
    n = int(input())
    adj = [list(map(int, input().split())) for _ in range(n)]
    result = [[] for _ in range(n)]

    # 90도 회전
    for i in range(n):
        string = ""
        for j in range(n - 1, -1, -1):
            string += str(adj[j][i])
        result[i].append(string)

    # 180도 회전
    for i in range(n - 1, -1, -1):
        string = ""
        for j in range(n - 1, -1, -1):
            string += str(adj[i][j])
        result[n - 1 - i].append(string)

    # 270도 회전
    for i in range(n - 1, -1, -1):
        string = ""
        for j in range(n):
            string += str(adj[j][i])
        result[n - 1 - i].append(string)

    # 출력
    print(f"#{t+1}")
    for i in result:
        print(*i, end=" ")
        print()
