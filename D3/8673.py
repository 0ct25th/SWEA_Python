from collections import deque

for t in range(int(input())):
    k = int(input())
    people = deque(map(int, input().split()))

    result = 0
    while k != 0:
        for i in range(0, len(people), 2):
            a = people.popleft()
            b = people.popleft()

            result += abs(a - b)

            people.append(max(a, b))

        k -= 1
    print(f"#{t+1} {result}")
