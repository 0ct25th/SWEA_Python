def back(idx, total):
    global result

    if idx == N:
        return

    total += A[idx]

    if total == K:
        result += 1

    back(idx + 1, total)
    back(idx + 1, total - A[idx])

for t in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0
    back(0, 0)
    print(f"#{t + 1} {result}")