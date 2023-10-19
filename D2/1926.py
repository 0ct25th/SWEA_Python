n = int(input())
nums = [str(i+1) for i in range(n)]

for i in range(n):
    cnt = 0
    for j in range(len(nums[i])):
        if int(nums[i][j]) % 3 == 0 and int(nums[i][j]) != 0:
            cnt += 1
    
    if cnt > 0:
        nums[i] = "-" * cnt
        
print(*nums)