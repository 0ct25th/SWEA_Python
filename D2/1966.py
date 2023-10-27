for t in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    print(f"#{t+1} ", end="")
    print(*nums)
