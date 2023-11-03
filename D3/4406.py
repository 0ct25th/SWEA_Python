for t in range(int(input())):
    string = input()
    print(f"#{t+1} ", end="")
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            continue
        else:
            print(i, end="")
    print()
