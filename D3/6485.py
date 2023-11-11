for t in range(int(input())):
    bus = [0] * 5001
    n = int(input())
    for _ in range(n):
        a, b = map(int ,input().split())
        for i in range(a, b + 1):
            bus[i] += 1
    
    p = int(input())
    result = []
    for _ in range(p):
        idx = int(input())
        result.append(bus[idx])
    print(f"#{t+1} ", end="")
    print(*result)