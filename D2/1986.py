for t in range(int(input())):
    n = int(input())
    nums = [i + 1 for i in range(n)]
    sum = 0
    for i in range(n):
        if nums[i] % 2 == 0:
            sum -= nums[i]
        else:
            sum += nums[i]

    print(f"#{t+1} {sum}")
