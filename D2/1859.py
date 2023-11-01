import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    days = list(map(int, input().split()))
    s_days = sorted([(value, day) for day, value in enumerate(days)], reverse=True)

    result, cnt = 0, 0
    for i in range(n):
        if days[i] == s_days[0][0]:
            continue
        # 사는 계산
        for j in range(n):
            # 해당일자가 더 싸다
            if days[i] < s_days[j][0]:
                # 일자가 앞서면
                if i < s_days[j][1]:
                    result -= days[i]  # 산다
                    cnt += 1
                    break  # 해당 일자에 한번 살 수 있으므로 종료
                # 일자가 뒤쳐지면 안산다

        # 파는 계산
        for j in range(n):
            # 해당일자가 더 싸다
            if days[i] < s_days[j][0]:
                # 일자가 앞서면 안사고 안팜
                # 일자가 뒤쳐지면
                if i < s_days[j][1]:
                    while cnt > 0:  # 판다
                        result += s_days[j][0]
                        cnt -= 1
                    break  # 일자 앞서고 가장 비싼날 팔았으므로 종료

    print(f"#{t+1} {result}")
