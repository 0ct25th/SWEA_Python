for tc in range(int(input())):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    if (int(month) == 1 and 0 < int(day) < 32) or (int(month) == 3 and 0 < int(day)) or (int(month) == 5 and 0 < int(day)) or (int(month) == 7 and 0 < int(day)) or (int(month) == 8 and 0 < int(day)) or (int(month) == 10 and 0 < int(day)) or (int(month) == 12 and 0 < int(day)):
            print(f"#{tc+1} {year}/{month}/{day}")
    elif int(month) == 2 and 0 < int(day) < 29:
            print(f"#{tc+1} {year}/{month}/{day}")
    elif (int(month) == 4 and 0 < int(day) < 31) or (int(month) == 6 and 0 < int(day) < 31) or (int(month) == 9 and 0 < int(day) < 31) or (int(month) == 11 and 0 < int(day) < 31):
            print(f"#{tc+1} {year}/{month}/{day}")
    else:
        print(f"#{tc+1} -1")
    