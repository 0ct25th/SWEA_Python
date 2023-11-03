for t in range(10):
    n = int(input())
    string = [list(map(int, input().split())) for _ in range(n)]

    col = []
    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += str(string[j][i])
        col.append(tmp.replace("0", ""))

    result = 0
    for i in range(len(col)):
        for j in range(len(col[i]) - 1):
            if len(col[i]) > 1:
                if len(col[i][j : j + 2]) > 1 and col[i][j : j + 2] == "12":
                    result += 1
            else:
                break

    print(f"#{t+1} {result}")
