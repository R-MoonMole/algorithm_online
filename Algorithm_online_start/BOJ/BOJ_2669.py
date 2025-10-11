import sys
sys.stdin = open('2669.txt', 'r')

visited = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = 1

for a in range(101):
    for b in range(101):
        if visited[a][b] == 1:
            result += 1

print(result)