from collections import deque

for _ in range(10):
    t = int(input())
    nums = deque(map(int, input().split()))

    minus = 1
    while True:
        if minus == 6:
            minus = 1

        tmp = nums.popleft()
        if tmp - minus > 0:
            nums.append(tmp - minus)
        else:
            nums.append(0)
            break

        minus += 1

    print(f"#{t}", end=" ")
    nums = list(nums)
    print(*nums)
