def r_palindrom(r, c):
    global result
    left, right = "", ""

    for i in range(n // 2):
        left += arr[r][c + i]
        right += arr[r][c + n - n // 2 + i]

    if left == right[::-1]:
        result += 1


def l_palindrom(r, c):
    global result
    left, right = "", ""

    for i in range(n // 2):
        left += arr[r + i][c]
        right += arr[r + n - n // 2 + i][c]

    if left == right[::-1]:
        result += 1


for t in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(8)]

    result = 0
    # 행에서 회문 찾기
    for i in range(8):
        for j in range(8 - n + 1):
            r_palindrom(i, j)

    # 열에서 회문 찾기
    for i in range(8 - n + 1):
        for j in range(8):
            l_palindrom(i, j)

    print(f"#{t+1} {result}")
