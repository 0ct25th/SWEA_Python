from collections import deque

for _ in range(10):
    t = int(input())
    dq = deque(map(int, input().split()))

    minus = 1
    while True:
        if minus == 6:
            minus = 1

        chk = dq.popleft() - minus
        if chk <= 0:
            dq.append(0)
            break
        else:
            dq.append(chk)

        minus += 1

    dq = list(dq)
    print(f"#{t} ", end="")
    print(*dq)
