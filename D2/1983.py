grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for t in range(int(input())):
    N, K = map(int, input().split())
    scores = []
    for _ in range(N):
        mid, final, hw = map(int, input().split())
        result = (mid * 0.35) + (final * 0.45) + (hw * 0.2)
        scores.append(result)

    # k번 학생의 점수 저장하기
    k_score = scores[K - 1]

    # 정렬
    scores.sort(reverse=True)
    div = N // 10
    # k 학생 점수를 정렬된 점수들의 인덱스로 찾아서
    # 학점을 구하기
    print(f"#{t+1} {grades[scores.index(k_score) // div]}")
