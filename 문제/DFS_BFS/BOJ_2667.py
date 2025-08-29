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

# DFS 순서
#
# DFS에 넣을걸 정함 -> 여기선 2개를 넣음(2중 배열이므로)
# visited[r][c]에 1을 넣음 -> visited도 2중 배열...
# count를 기본 1로 바꿈(한개 들어온거니까)
# 4방향으로 반복문
# 0 <= nr , cr < N 해서 arr의 배열을 넘어가지 않은 선에서...
# visited[nr][nc]가 0(방문하지 않았고)이고 arr[nr][nc]가 1 일때(단지가 있을 때)
# count에 DFS(nr, nc)가 더해지게 되는데 여기서 DFS(nr, nc)는
# 애초에 조건이 방문하지 않고 단지가 있을때만 들어가는 조건이라
# return count에서 1이 return이 되어서
# count += 1이 되는 형식...
#
#
#
#
#

