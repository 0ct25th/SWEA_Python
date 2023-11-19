for t in range(10):
    # 항상 100이 들어오며 테이블의 크기를 나타냄
    N = int(input())
    # 테이블의 초기 상태
    table = [list(map(int, input().split())) for _ in range(N)]

    # 열마다 문자열로 만들기
    mutex = []
    for i in range(N):
        string = ""
        for j in range(N):
            string += str(table[j][i])
        # 0제거해 N=1, S=2만 남겨두기
        string = string.replace('0', '')
        # 문자열 string을 정수 배열로 변경해 저장하기
        mutex.append(list(map(int, string)))

    result = 0
    for i in range(len(mutex)):
        if len(mutex[i]) > 1:
            for j in range(len(mutex[i]) - 1):
                if mutex[i][j] == 1 and mutex[i][j + 1] == 2:
                    result += 1

    print(f"#{t + 1} {result}")
