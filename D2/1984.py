for t in range(int(input())):
    nums = sorted(list(map(int, input().split())))
    del nums[0]
    del nums[-1]
    result = round(sum(nums) / 8)
    print(f"#{t+1} {result}")
