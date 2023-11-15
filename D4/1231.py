def inord(n):
    if n <= N:
        # 왼쪽 자식 순회
        inord(n * 2)
        result.append(word[n])
        # 오른쪽 자식 순회
        inord(n * 2 + 1)

for t in range(10):
    N = int(input())
    # 문자를 자신의 번호 인덱스에 맞춰 저장
    word = [0] * (N + 1)

    # 각 번호에 맞춰 문자 저장
    for _ in range(N):
        string = list(input().split())
        word[int(string[0])] = string[1]

    # 중위 순회
    result = []
    inord(1)
    print(f"#{t+1} {''.join(result)}")