op_pri = {'*': 2, '+':1}

for t in range(10):
    N = int(input())
    string = input()

    # 중위 표기식 -> 후위 표기식 변경
    op_stk = []
    postfix = ""
    for i in string:
        if i.isdigit():
            postfix += i
        else:
            while op_stk and op_pri[i] <= op_pri[op_stk[-1]]:
                postfix += op_stk.pop()
            op_stk.append(i)

    while op_stk:
        postfix += op_stk.pop()

    # 후위 표기식 연산
    result = []
    for i in postfix:
        if i.isdigit():
            result.append(i)
        else:
            a = int(result.pop())
            b = int(result.pop())
            if i == '+':
                result.append(a+b)
            else:
                result.append(a*b)
    print(f"#{t + 1} ", end="")
    print(*result)