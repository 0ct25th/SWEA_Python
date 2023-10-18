t = int(input())

for tc in range(t):
    nums = list(map(int, input().split()))

    print(f"#{tc+1} {round(sum(nums)/len(nums))}")
