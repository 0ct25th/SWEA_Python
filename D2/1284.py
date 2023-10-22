for t in range(int(input())):
    P, Q, R, S, W = map(int, input().split())

    costA, costB = W * P, Q
    if R < W:
        costB += S * (W - R)
    print(f"#{t+1} {min(costA, costB)}")
