# BOJ_8979 : 올림픽
# https://www.acmicpc.net/problem/8979

N, K = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

K_idx = -1
for i in range(N):
    if arr[i][0] == K:
        K_idx = i
        break

status = [0] * N
status[K_idx] = 3

for i in range(1, 4):
    for j in range(N):
        if status[j] != 0:
            continue

        a = arr[j][i]
        b = arr[K_idx][i]
        if a > b:
            status[j] = 1
        elif a < b:
            status[j] = -1

rank = 1
for k in status:
    if k == 1:
        rank += 1

print(rank)