for t in range(10):
    n, string = input().split()

    while True:
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                string = string[0:i] + string[i + 2 :]
                break
            else:
                chk = i
        if chk == len(string) - 2:
            break

    print(f"#{t+1} {string}")
