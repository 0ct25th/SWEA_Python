def Back(cur):
    global result
    if cur == n:
        result += 1
        return

    for i in range(n):
        if Visited_row[i] or Visited_r_crs[cur- i + n - 1] or Visited_l_crs[cur + i]:
            continue
        
        Visited_row[i] = True
        Visited_r_crs[cur-i+n-1] = True
        Visited_l_crs[cur+i] = True
            
        Back(cur + 1)
        
        Visited_row[i] = False
        Visited_r_crs[cur-i+n-1] = False
        Visited_l_crs[cur+i] = False


for t in range(int(input())):
    n = int(input())

    Visited_row = [False] * n
    Visited_r_crs = [False] * n * 2
    Visited_l_crs = [False] * n * 2

    result = 0
    Back(0)
    print(f"#{t+1} {result}")
