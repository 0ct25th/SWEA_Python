def back(n):  # 교환 횟수를 인자로 받는 재귀 함수입니다.
    global result  # 전역 변수 result를 사용하기 위해 선언합니다.
    if n == N:  # 교환 횟수가 주어진 횟수와 같아지면
        result = max(
            result, int("".join(map(str, arr)))
        )  # 현재 배열로 만들 수 있는 수와 이전의 최대값 중 더 큰 값을 result에 저장합니다.
        return  # 재귀 함수를 종료합니다.

    for i in range(len(arr) - 1):  # 배열의 첫 원소부터 끝에서 두 번째 원소까지 반복합니다.
        for j in range(i + 1, len(arr)):  # i번째 원소 다음 원소부터 마지막 원소까지 반복합니다.
            arr[i], arr[j] = arr[j], arr[i]  # i번째 원소와 j번째 원소를 교환합니다.

            chk = (
                "".join(map(str, arr)) + "_" + str(n)
            )  # 현재 배열로 만들 수 있는 수에 교환 횟수를 더한 값을 chk에 저장합니다.
            if chk not in Visited:  # chk가 방문한 적 없는 값이면
                back(n + 1)  # 교환 횟수를 하나 늘려서 재귀 함수를 호출합니다.
                Visited.append(chk)  # chk를 방문한 값으로 추가합니다.

            arr[i], arr[j] = arr[j], arr[i]  # 원래대로 원소를 돌려놓습니다.


for t in range(int(input())):  # 주어진 테스트 케이스의 수만큼 반복합니다.
    string, cnt = input().split()  # 숫자를 문자열 형태로 받고, 교환 횟수를 받습니다.
    N = int(cnt)  # 교환 횟수를 정수형으로 변환합니다.
    arr = list(map(int, list(string)))  # 문자열을 숫자로 변환하여 배열에 저장합니다.
    result = 0  # 최대값을 저장할 변수를 초기화합니다.
    Visited = []  # 방문한 값들을 저장할 배열을 초기화합니다.
    back(0)  # 교환 횟수를 0으로 하여 재귀 함수를 호출합니다.
    print(f"#{t+1} {result}")  # 테스트 케이스 번호와 최대값을 출력합니다.
