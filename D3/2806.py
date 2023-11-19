def back(cur):
    global result

    if cur == N:
        result += 1
        return

    for col in range(N):
        if not Visited1[col] and not Visited2[col + cur] and not Visited3[col - cur + N - 1]:
            Visited1[col] = True
            Visited2[col + cur] = True
            Visited3[col - cur + N - 1] = True

            back(cur + 1)

            Visited1[col] = False
            Visited2[col + cur] = False
            Visited3[col - cur + N - 1] = False


for t in range(int(input())):
    N = int(input())
    # 같은 열에 존재하는지 확인하는 배열
    Visited1 = [False] * N
    # 같은 왼쪽 대각선에 존재하는지 확인하는 배열 c + r
    Visited2 = [False] * N * 2
    # 같은 오른쪽 대각선에 존재하는지 확인하는 배열 c - r + N - 1
    Visited3 = [False] * N * 2

    result = 0
    back(0)

    print(f"#{t + 1} {result}")