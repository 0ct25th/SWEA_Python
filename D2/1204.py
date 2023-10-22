for _ in range(int(input())):
    t = int(input())

    student = list(map(int, input().split()))
    dir = dict()
    for i in range(len(student)):
        if student[i] in dir.keys():
            dir[student[i]] += 1
        else:
            dir[student[i]] = 1

    dir = sorted(dir.items(), key=lambda x: x[1], reverse=True)

    result = [dir[0][0]]
    for i in range(1, len(dir)):
        if dir[0][1] == dir[i][1]:
            result.append(dir[i][0])
    print(f"#{t} {max(result)}")
