for t in range(int(input())):
    cur_a, cur_b = 1, 1
    string = input()
    for i in string:
        if i == "L":
            cur_b = cur_a + cur_b
        else:
            cur_a = cur_a + cur_b

    print(f"#{t+1} {cur_a} {cur_b}")
