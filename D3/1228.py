n = int(input())
original = list(map(int, input().split()))
command_cnt = int(input())
command = list(input().split())

tmp = [[] for _ in range(command_cnt)]
cnt, idx = 0, 0
while True:
    if idx == len(command):
        break
