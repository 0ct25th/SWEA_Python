from collections import deque

for t in range(10):
    n = int(input())
    original = list(map(int, input().split()))
    command_cnt = int(input())
    command = [[] for _ in range(command_cnt)]
    tmp = deque(input().split())

    i = -1
    while i != command_cnt:
        if len(tmp) == 0:
            break

        if tmp[0] == "I" or tmp[0] == "D" or tmp[0] == "A":
            i += 1
            command[i].append(tmp[0])
            tmp.popleft()
        else:
            command[i].append(tmp[0])
            tmp.popleft()

    # 명령어 개수만큼 실행

    for i in range(len(command)):
        chk = command[i][0]
        x = int(command[i][1])
        y = int(command[i][2])
        s = command[i][3:]
        if chk == "I":
            for j in range(y):
                original.insert(x, int(s[j]))
                x += 1
        elif chk == "D":
            for _ in range(y):
                del original[x]

    print(f"#{t+1} ", end="")
    print(*original[:10])
