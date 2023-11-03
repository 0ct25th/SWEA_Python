for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    up_value, down_value = 0, 0
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            up_value = max(up_value, abs(lst[i] - lst[i + 1]))
        else:
            down_value = max(down_value, abs(lst[i] - lst[i + 1]))
    print(f"#{t+1} {down_value} {up_value}")
