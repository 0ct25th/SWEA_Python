for t in range(int(input())):
    memory = list(input())

    flag = memory[0]
    
    if flag != '0':
        result = 1
    else:
        result = 0
        
    for i in range(1, len(memory)):
        if flag != memory[i]:
            result += 1
            flag = memory[i]
            
    print(f"#{t+1} {result}")