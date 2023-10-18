for tc in range(int(input())):
    a, b = map(int, input().split())
    print(f"#{tc+1} {a//b} {a%b}")