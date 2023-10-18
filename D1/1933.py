n = int(input())

stk = []
for i in range(1, n+1):
    if n % i == 0:
        stk.append(i)

print(*stk)