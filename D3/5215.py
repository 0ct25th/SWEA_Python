def Back(idx, cur_t, cur_k):
    global max_taste
    if cur_k > L:
        return
    
    if idx == N:
        max_taste = max(max_taste, cur_t)
        return

    # 현재 메뉴를 선택하는 경우
    Back(idx + 1, cur_t + m[idx][0], cur_k + m[idx][1])
    # 현재 메뉴를 선택하지 않는 경우
    Back(idx + 1, cur_t, cur_k)


for t in range(int(input())):
    N, L = map(int, input().split())

    m = []
    for _ in range(N):
        T, K = map(int, input().split())
        m.append((T, K))

    max_taste = 0
    Back(0, 0, 0)
    print(f"#{t+1} {max_taste}")
