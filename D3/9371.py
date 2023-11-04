for t in range(int(input())):
    n = int(input())
    string = input()
    sc_string = input()

    result = 0
    for i in range(n):
        if string[i] == sc_string[i]:
            result += 1

    print(f"#{t+1} {result}")
