for t in range(int(input())):
    string = input()

    st, en = 0, len(string) - 1
    chk = True
    while st < en:
        if string[st] != string[en]:
            chk = False
            break
        st += 1
        en -= 1
    if chk:
        print(f"#{t + 1} {1}")
    else:
        print(f"#{t + 1} {0}")
