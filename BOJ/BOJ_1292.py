# BOJ_1292 : 쉽게 푸는문제
# https://www.acmicpc.net/problem/1292

A, B = map(int, input().split())

N = 1000
arr = []
num = 1
result = 0

while len(arr) < N:
    for _ in range(num):
        arr.append(num)
        if len(arr) == N:
            break
    num += 1

for i in arr[A-1:B]:
    result += i

print(result)