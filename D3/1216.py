def r_palindrom(r, c):
    left, right = "", ""

    for i in range(n // 2):
        left += arr[r][c + i]
        right += arr[r][c + n - n // 2 + i]

    if left == right[::-1]:
        return True
    else:
        return False


def l_palindrom(r, c):
    global result
    left, right = "", ""

    for i in range(n // 2):
        left += arr[r + i][c]
        right += arr[r + n - n // 2 + i][c]

    if left == right[::-1]:
        return True
    else:
        return False


for _ in range(10):
    t = int(input())
    arr = [list(input()) for _ in range(100)]

    result = -1e9
    right, left = -1e9, -1e9
    for n in range(10, 100):  # 행에서 회문 찾기
        for i in range(100):
            for j in range(100 - n + 1):
                if r_palindrom(i, j):
                    right = max(right, n)

        # 열에서 회문 찾기
        for i in range(100 - n + 1):
            for j in range(100):
                if l_palindrom(i, j):
                    left = max(left, n)

        result = max(right, left)

    print(f"#{t} {result}")
