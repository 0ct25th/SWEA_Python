for t in range(int(input())):
    n = int(input())

    nums = set(int(i) for i in str(n))
    sum = n

    while len(nums) != 10:
        sum = n + int(sum)
        for i in str(sum):
            nums.add(int(i))

    print(f"#{t+1} {sum}")
