for tc in range(int(input())):
    nums = list(map(int, input().split()))

    print(f"#{tc+1} {round(sum(nums)/len(nums))}")
