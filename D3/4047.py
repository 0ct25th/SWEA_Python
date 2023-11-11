for t in range(int(input())):
    S = input()
    card = []

    # 카드 3자리씩 분류
    for i in range(0, len(S), 3):
        card.append(S[i:i+3])

    result = [[False] * 13 for _ in range(4)]
    chk = True
    # 카드 무늬, 숫자 분류
    for i in range(len(card)):
        pattern = card[i][0]
        num = int(card[i][1] + card[i][2]) - 1

        if pattern == 'S':
            if not result[0][num]:
                result[0][num] = True
            else:
                print(f"#{t+1} ERROR")
                chk = False
                break
        if pattern == 'D':
            if not result[1][num]:
                result[1][num] = True
            else:
                print(f"#{t+1} ERROR")
                chk = False
                break
        if pattern == 'H':
            if not result[2][num]:
                result[2][num] = True
            else:
                print(f"#{t+1} ERROR")
                chk = False
                break
        if pattern == 'C':
            if not result[3][num]:
                result[3][num] = True
            else:
                print(f"#{t+1} ERROR")
                chk = False
                break

    # 무늬별로 몇 장 부족한지 출력
    output = []
    for i in range(4):
        tmp = 13
        for j in range(13):
            if result[i][j]:
                tmp -= 1
        output.append(tmp)

    if chk:
        print(f"#{t + 1}", end=" ")
        print(*output)
