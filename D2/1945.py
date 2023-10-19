for t in range(int(input())):
    num = int(input())
    stk = [0, 0, 0, 0, 0]
    while num:
        if num % 2 == 0:
            num //= 2
            stk[0] += 1
        elif num % 3 == 0:
            num //= 3
            stk[1] += 1
        elif num % 5 == 0:
            num //= 5
            stk[2] += 1
        elif num % 7 == 0:
            num //= 7
            stk[3] += 1
        elif num % 11 == 0:
            num //= 11
            stk[4] += 1
        else:
            break

    print(f"#{t+1}", end=" ")
    print(*stk)