n = int(input())
nums = list(map(int, input().split()))
nums.sort()
mid = nums[len(nums)//2]
print(mid)
