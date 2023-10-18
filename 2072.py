t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    sum = 0

    for j in nums:
        if j % 2 != 0:
            sum += j

    print(f"#{i+1} {sum}")
