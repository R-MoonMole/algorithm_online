# BOJ_2477 : 참외밭
# https://www.acmicpc.net/problem/2477

K = int(input())
dirs = []
lent = []
count = [0] * 5

for _ in range(6):
    A, B = map(int, input().split())
    dirs.append(A)
    lent.append(B)

for i in range(6):
    count[dirs[i]] += 1

lg_sq = 1
for a, b in zip(dirs, lent):
    if count[a] == 1:
        lg_sq *= b

sm_sq = 0
for j in range(6):
    if dirs[j] == dirs[(j+2) % 6]:
        sm_sq = lent[(j+1) % 6] * lent[(j+2) % 6]
        break
result = (lg_sq - sm_sq) * K


print(result)