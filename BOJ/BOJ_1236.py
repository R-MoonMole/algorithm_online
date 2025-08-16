# BOJ_1236 : 성 지키기
# https://www.acmicpc.net/problem/1236

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

wid_count = 0
len_count = 0
result = 0

for i in range(N):
    count = 0
    for j in range(M):
        if arr[i][j] == '.':
            count += 1
            if count == M:
                wid_count += 1

for j in range(M):
    count = 0
    for i in range(N):
        if arr[i][j] == '.':
            count += 1
            if count == N:
                len_count += 1

if wid_count > len_count:
    result = wid_count
else:
    result = len_count

print(result)