for t in range(10):
    cnt = int(input())
    box = list(map(int, input().split()))
    # 초기 최대, 최소값의 인덱스 값 정의
    max_height = box.index(max(box))
    min_height = box.index(min(box))

    for _ in range(cnt):
        box[max_height] -= 1
        box[min_height] += 1
        # 최대, 최소값의 인덱스 값 재정의
        max_height = box.index(max(box))
        min_height = box.index(min(box))

    print(f"#{t+1} {box[max_height] - box[min_height]}")
