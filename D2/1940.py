for t in range(int(input())):
    dist, speed = 0, 0
    for _ in range(int(input())):
        string = input()
        if len(string) > 1:
            a, b = map(int, string.split())
            if a == 1:
                speed += b
                dist += speed
            else:
                if speed < b:
                    speed = 0
                else:
                    speed -= b
                dist += speed
        else:
            dist += speed
    print(f"#{t+1} {dist}")
