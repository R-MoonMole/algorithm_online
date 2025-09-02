# BOJ_2477 : 참외밭
# https://www.acmicpc.net/problem/2477

K = int(input())
dirs = []
lens = []
max_w, max_h = 0, 0
w = h = -1


for _ in range(6):
    A, B = map(int, input().split())
    dirs.append(A)
    lens.append(B)

for i in range(6):
    if dirs[i] in (1,2):
        if lens[i] > max_w:
            max_w = lens[i]
            w = i
    else:
        if lens[i] > max_h:
            max_h = lens[i]
            h = i
lg_sq = max_w * max_h

sm_sq = lens[(w+3)%6] * lens[(h+3)%6]

print((lg_sq - sm_sq) * K)