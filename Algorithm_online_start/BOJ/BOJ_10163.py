import sys
sys.stdin = open('10163.txt', 'r')

N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
number = [0] * (N + 1)

for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        arr[j][x:(x+w)] = [i]*w


for a in range(1001):
    for b in range(1001):
        if arr[a][b] != 0:
            number[arr[a][b]] += 1

for l in range(1, N+1):
    print(number[l])

