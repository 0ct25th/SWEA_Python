for t in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    avg = sum(d) // n

    result = 0
    for i in d:
        if i <= avg:
            result += 1
    print(f"#{t+1} {result}")
