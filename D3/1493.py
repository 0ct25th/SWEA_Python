# key: 값, value: 좌표
v_dict = dict()
# key: 좌표, value: 값
c_dict = dict()

i, j = 1, 1
for k in range(1, 50000):
    v_dict[k] = (i, j)
    c_dict[(i, j)] = k

    i -= 1
    j += 1
    if i < 1:
        i = j
        j = 1

for t in range(int(input())):
    p, q = map(int, input().split())

    # &(p)
    and_p = v_dict[p]
    # &(q)
    and_q = v_dict[q]
    # #(&(p) + &(q)) = #((x, y) + (z, w)) = #((x+z), (y+w))
    s_coord =(and_p[0] + and_q[0], and_p[1] + and_q[1])
    result = c_dict[s_coord]
    print(f"#{t+1} {result}")
