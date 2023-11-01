for t in range(10):
    n = int(input())
    arr = list(map(int, input().split()))

    result = []
    for i in range(2, len(arr) - 2):
        max_height = max(max(arr[i - 2], arr[i - 1]), max(arr[i + 1], arr[i + 2]))
        if max_height < arr[i]:
            result.append(arr[i] - max_height)

    print(f"#{t+1} {sum(result)}")
