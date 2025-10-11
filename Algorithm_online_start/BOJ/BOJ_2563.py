import sys
sys.stdin = open ('2563.txt', 'r')

N = int(input())
lst = []
result = 0

visited = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            visited[i][j] = 1

for a in range(100):
    for b in range(100):
        if visited[a][b] == 1:
            result += 1

print(result)