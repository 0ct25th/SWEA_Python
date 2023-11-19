for t in range(int(input())):
    N, M, K = map(int, input().split())
    time = sorted(list(map(int, input().split())))

    result = "Possible"
    people = 0
    for i in time:
        people += 1
        if i // M * K < people:
            result = "Impossible"
            break

    print(f"#{t + 1} {result}")
