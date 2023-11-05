for t in range(int(input())):
    n, k = map(int, input().split())
    not_hw = [i + 1 for i in range(n)]
    hw = list(map(int, input().split()))

    print(f"#{t+1} ", end="")
    for i in range(n):
        if not_hw[i] not in hw:
            print(not_hw[i], end=" ")
    print()
