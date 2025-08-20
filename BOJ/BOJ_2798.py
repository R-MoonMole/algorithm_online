# BOJ_2798 : 블랙잭
# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
arr = list(map(int, input().split()))
large_M = 0
real = 0
x, y, z, = 0, 0, 0

for i in range(N-2):
    for j in range(1, N-1):
        for k in range(2, N):
            if i != j and j != k and i != k:
                if arr[i]+arr[j]+arr[k] <= M:
                    large_M = arr[i]+arr[j]+arr[k]
                    if large_M > real:
                        real = large_M
                        x = i
                        y = j
                        z = k

print(arr[x]+arr[y]+arr[z])