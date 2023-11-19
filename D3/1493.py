# 키: 좌표, 값: 해당 좌표 값
coord = dict()
# 키: 좌표 내 값, 값: 값에 해당하는 좌표
val = dict()

x, y = 1, 1
for n in range(1, 50000):
    coord[(x, y)] = n
    val[n] = (x, y)

    x, y = x + 1, y - 1

    if y < 1:
        y, x = x, 1

for t in range(int(input())):
    p, q = map(int, input().split())

    # &(p) = #(x, y)
    x, y = val[p][0], val[p][1]
    # &(q) = #(z, w)
    z, w = val[q][0], val[q][1]

    # #(&(p)+&(q)) = #((x, y)+(z, w)) = #((x + z), (y + w))
    xz = x + z
    yw = y + w

    # (xz, yw)의 값 저장하기
    result = coord[(xz, yw)]

    print(f"#{t + 1} {result}")


