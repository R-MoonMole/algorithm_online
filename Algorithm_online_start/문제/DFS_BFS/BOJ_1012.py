'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

'''

# BOJ_1012 : 유기농 배추
# https://www.acmicpc.net/problem/1012

T = int(input())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]


    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1


    def DFS(sr, sc):
        stack = [(sr, sc)]
        visited[sr][sc] = 1
        while stack:
            r, c = stack.pop()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if visited[nr][nc] == 0 and field[nr][nc] == 1:
                        visited[nr][nc] = 1
                        stack.append((nr, nc))

    worms = 0
    for j in range(N):
        for k in range(M):
            if field[j][k] == 1 and visited[j][k] == 0:
                DFS(j, k)
                worms += 1

    print(worms)