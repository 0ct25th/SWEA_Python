for t in range(int(input())):
    N, Q = map(int, input().split())

    box = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box[j] = i + 1

    print(f"#{t + 1}", end=" ")
    print(*box)