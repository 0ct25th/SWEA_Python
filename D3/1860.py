for t in range(int(input())):
    n, m, k = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    
    result = 'Possible'
    sec = 0
    for i in p:
        sec += 1
        if i // m * k < sec:
            result = 'Impossible'
            break

    
    print(f"#{t+1} {result}")
    