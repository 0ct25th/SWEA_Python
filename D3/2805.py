for t in range(int(input())):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    result = 0
    for i in range(n):
        if i <= n// 2:
            for j in range(n//2 - i,n//2 + i +1):
                result += farm[i][j]
        else:
            for j in range(n//2 - (n//2 +n//2 - i),n//2 +(n//2 +n//2 - i)+1):
                result += farm[i][j]
    print(f"#{t+1} {result}")