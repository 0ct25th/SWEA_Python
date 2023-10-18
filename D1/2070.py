for tc in range(int(input())):
    a, b = map(int, input().split())

    if a > b:
        print(f"#{tc+1} >")
    elif a < b:
        print(f"#{tc+1} <")
    else:
        print(f"#{tc+1} =")
        
        