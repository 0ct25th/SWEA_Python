key_dict = {
    "0001101": 0,
    "1110010": 0,
    "0011001": 1,
    "1100110": 1,
    "0010011": 2,
    "1101100": 2,
    "0111101": 3,
    "1000010": 3,
    "0100011": 4,
    "1011100": 4,
    "0100011": 4,
    "0110001": 5,
    "1001110": 5,
    "0101111": 6,
    "1010000": 6,
    "0111011": 7,
    "1000100": 7,
    "0110111": 8,
    "1001000": 8,
    "0001011": 9,
    "1110100": 9,
}

for t in range(int(input())):
    n, m = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(n)]

    for i in board:
        if 1 in i:
            tmp = i
            break

    # 뒷 0 제거
    for i in range(m - 1, -1, -1):
        if tmp[i] != 1:
            tmp.pop()
        else:
            break

    # 반전 후
    tmp = tmp[::-1]
    # 뒷 0 제거
    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i] != 1:
            tmp.pop()
        else:
            break

    # 56개 만들기
    while len(tmp) != 56:
        tmp.append(0)
    tmp = tmp[::-1]

    secret = ""
    for i in tmp:
        secret += str(i)

    result = []
    for i in range(0, 56, 7):
        string = secret[i : i + 7]
        result.append(key_dict[string])

    even, odd = 0, 0
    for i in range(8):
        if (i + 1) % 2 == 0:
            even += result[i]
        else:
            odd += result[i] * 3

    if (even + odd) % 10 == 0:
        print(f"#{t+1} {sum(result)}")
    else:
        print(f"#{t+1} 0")
