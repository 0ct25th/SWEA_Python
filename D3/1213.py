for _ in range(10):
    t = int(input())
    word = input()
    string = input()

    cnt = 0
    for i in range(0, len(string) - len(word) + 1):
        if word == string[i : i + len(word)]:
            cnt += 1
    print(f"#{t} {cnt}")
