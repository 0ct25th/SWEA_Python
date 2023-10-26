for t in range(int(input())):
    string = input()

    result = string[0]
    for i in range(1, 10):
        result += string[i]
        if result == string[i + 1 : (i + 1) * 2]:
            break

    print(f"#{t+1} {len(result)}")
