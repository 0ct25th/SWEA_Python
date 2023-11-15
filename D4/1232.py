def postord(n):
    if word[n]:
        if word[n] == '+':
            return postord(ch1[n]) + postord(ch2[n])
        elif word[n] == '-':
            return postord(ch1[n]) - postord(ch2[n])
        elif word[n] == '*':
            return postord(ch1[n]) * postord(ch2[n])
        elif word[n] == '/':
            return postord(ch1[n]) / postord(ch2[n])
        else:
            return int(word[n])
    else:
        return 0


for t in range(10):
    N = int(input())
    # 숫자, 연산자 모두 저장
    word = [0] * (N + 1)
    # 해당 인덱스의 왼쪽 자식 저장
    ch1 = [0] * (N + 1)
    # 해당 인덱스의 오른쪽 자식 저장
    ch2 = [0] * (N + 1)

    for _ in range(N):
        string = list(input().split())

        word[int(string[0])] = string[1]
        if len(string) > 2:
            ch1[int(string[0])] = int(string[2])
            ch2[int(string[0])] = int(string[3])

    result = postord(1)
    print(f"#{t + 1} {int(result)}")