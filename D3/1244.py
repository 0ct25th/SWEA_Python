def back(n):  # 교환 횟수를 인자로 받는 재귀 함수입니다.
    global result

    # 종료 조건
    if n > N:
        result = max(result, int(''.join(map(str, P))))
        return

    for i in range(len(P) - 1):
        for j in range(i + 1, len(P)):
            P[i], P[j] = P[j], P[i]
            chk = ''.join(map(str, P)) + "_" + str(n)

            if chk not in Visited:
                back(n + 1)
                Visited.append(chk)

            # 재귀 후 다시 스왑
            P[i], P[j] = P[j], P[i]


for t in range(int(input())):  # 주어진 테스트 케이스의 수만큼 반복합니다.
    string, cnt = input().split()
    N = int(cnt)    # 교환 가능 횟수
    P = list(map(int, string))  # 상금 배열

    result = 0
    Visited = []
    back(1)
    print(f"#{t + 1} {result}")
