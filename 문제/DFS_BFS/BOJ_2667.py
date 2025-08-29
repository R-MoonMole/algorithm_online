N = int(input())

arr = [list(map(int, input().strip())) for _ in range(N)]
dr = [1, 0, -1, 0] # 우측부터 시계방향
dc = [0, 1, 0, -1]
visited = [[0] * N for _ in range(N)]
result = []

def DFS(r, c):
    visited[r][c] = 1
    count = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                count += DFS(nr, nc)
    return count

for j in range(N):
    for k in range(N):
        if arr[j][k] == 1 and visited[j][k] == 0:
            result.append(DFS(j, k))

result.sort()
print(len(result))
for row in result:
    print(row)