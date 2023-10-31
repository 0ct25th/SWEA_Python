for t in range(int(input())):
    n = int(input())

    result = ""
    for i in range(n):
        word, num = map(str, input().split())
        result += word * int(num)

    print(f"#{t+1}")
    for i in range(0, len(result), 10):
        print(result[i : i + 10])
