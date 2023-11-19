for t in range(10):
    dump = int(input())
    box = sorted(list(map(int, input().split())))

    while dump != 0:
        box[0] += 1
        box[-1] -= 1
        dump -= 1
        box.sort()

    print(f"#{t + 1} {max(box) - min(box)}")