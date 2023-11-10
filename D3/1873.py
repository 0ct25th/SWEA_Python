from collections import deque

def is_valid_coord(r, c):
    return -1<r<H and -1<c<W

def move(direction, r, c):
    if direction == '^':
        if is_valid_coord(r-1, c) and adj[r-1][c] == '.':
            adj[r][c] = '.'
            adj[r-1][c] = '^'
            return r-1, c
    elif direction == 'v':
        if is_valid_coord(r+1, c) and adj[r+1][c] == '.':
            adj[r][c] = '.'
            adj[r+1][c] = 'v'
            return r+1, c
    elif direction == '<':
        if is_valid_coord(r, c-1) and adj[r][c-1] == '.':
            adj[r][c] = '.'
            adj[r][c-1] = '<'
            return r, c-1
    elif direction == '>':
        if is_valid_coord(r, c+1) and adj[r][c+1] == '.':
            adj[r][c] = '.'
            adj[r][c+1] = '>'
            return r, c+1
        
    adj[r][c] = direction
    return r, c


def u_attack(sr, sc):
    dq = deque()
    dq.append((sr, sc))
    
    while len(dq):
        r, c = dq.popleft()
        
        if adj[r][c] == '*':
            adj[r][c] = '.'
            return
        elif adj[r][c] == '#':
            return
        
        nr = r - 1
        nc = c
        if is_valid_coord(nr, nc):
            dq.append((nr, nc))
        
        
def d_attack(sr, sc):
    dq = deque()
    dq.append((sr, sc))
    
    while len(dq):
        r, c = dq.popleft()
        
        if adj[r][c] == '*':
            adj[r][c] = '.'
            return
        elif adj[r][c] == '#':
            return
        
        nr = r + 1
        nc = c
        if is_valid_coord(nr, nc):
            dq.append((nr, nc))
            
            
def l_attack(sr, sc):
    dq = deque()
    dq.append((sr, sc))
    
    while len(dq):
        r, c = dq.popleft()
        
        if adj[r][c] == '*':
            adj[r][c] = '.'
            return
        elif adj[r][c] == '#':
            return
        
        nr = r
        nc = c - 1
        if is_valid_coord(nr, nc):
            dq.append((nr, nc))
            
            
def r_attack(sr, sc):
    dq = deque()
    dq.append((sr, sc))
    
    while len(dq):
        r, c = dq.popleft()
        
        if adj[r][c] == '*':
            adj[r][c] = '.'
            return
        elif adj[r][c] == '#':
            return
        
        nr = r
        nc = c + 1
        if is_valid_coord(nr, nc):
            dq.append((nr, nc))


for t in range(int(input())):
    H, W = map(int, input().split())
    adj = [list(input()) for _ in range(H)]
    N= int(input())
    command = list(input())

    for i in range(H):
        for j in range(W):
            if adj[i][j] == '^' or adj[i][j] == 'v' or adj[i][j] == '<' or adj[i][j] == '>':
                r, c = i, j
                direction = adj[i][j]
                break
                
    for i in range(N):
        if command[i] == 'U':
            direction = "^"
            r, c = move(direction, r, c)
        elif command[i] == 'D':
            direction = "v"
            r, c = move(direction, r, c)
        elif command[i] == 'L':
            direction = "<"
            r, c = move(direction, r, c)
        elif command[i] == 'R':
            direction = ">"
            r, c = move(direction, r, c)
        elif command[i] == 'S':
            if direction == '^':
                u_attack(r, c)
            elif direction == 'v':
                d_attack(r, c)
            elif direction == '<':
                l_attack(r, c)
            elif direction == '>':
                r_attack(r, c)
            
    print(f"#{t+1} ", end="")
    for lst in adj:
        print(*lst, sep="", end="")
        print()