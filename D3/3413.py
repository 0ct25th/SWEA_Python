for t in range(int(input())):
    L, U, X = map(int, input().split())

    if U < X:
        print(f"#{t+1} {-1}")
    elif L < X:
        print(f"#{t+1} {0}")
    else:
        print(f"#{t+1} {L-X}")
