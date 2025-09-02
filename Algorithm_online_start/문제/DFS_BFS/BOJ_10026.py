# BOJ_10026 : 적록색약
# https://www.acmicpc.net/problem/10026

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

dr = [1, 0, -1, 0] # 우측부터 시계방향
dc = [0, 1, 0, -1]
visited = [[0] * N for _ in range(N)]

def DFS_iter(sr, sc, color, visited):
    stack = [(sr, sc)]
    visited[sr][sc] = 1
    while stack:
        r, c = stack.pop()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and arr[nr][nc] == color:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))

normal = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS_iter(i, j, arr[i][j], visited)
            normal += 1


for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0] * N for _ in range(N)]
red_green = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS_iter(i, j, arr[i][j], visited)
            red_green += 1

print(normal, red_green)



































































# 이 방법은 재귀 깊이로 인한 RecursionError발생함...

# N = int(input())
# arr = [list(input().strip()) for _ in range(N)]
#
# dr = [1, 0, -1, 0] # 우측부터 시계방향
# dc = [0, 1, 0, -1]
# visited = [[0] * N for _ in range(N)]
#
# def DFS(r, c, color):
#     visited[r][c] = 1
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if 0 <= nr < N and 0 <= nc < N:
#             if not visited[nr][nc] and arr[nr][nc] == color:
#                 DFS(nr, nc, color)
#
# normal = 0
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             DFS(i, j, arr[i][j])
#             normal += 1
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 'R':
#             arr[i][j] = 'G'
#
# visited = [[0] * N for _ in range(N)]
# red_green = 0
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             DFS(i, j, arr[i][j])
#             red_green += 1
#
# print(normal, red_green)