import sys; sys.stdin = open('input.txt')

for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    sp_x, sp_y, ep_x, ep_y = 0, 0, 0, 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                sp_x, sp_y = i, j
            if arr[i][j] == 3:
                ep_x, ep_y = i, j

    def bfs(i, j, N):
        visited = [[0] * N for _ in range(N)]
        Q = []
        Q.append([i, j])
        visited[i][j] = 1

        while Q:
            ti, tj = Q.pop(0)
            if arr[ti][tj] == 3:
                return 1
            for di, dj in [[1,0], [0,-1], [-1,0], [0,1]]:
                wi, wj = ti+di, tj+dj
                if 0 <= wi < N and 0 <= wj < N and arr[wi][wj] != 1 and visited[wi][wj] == 0:
                    Q.append([wi, wj])
                    visited[wi][wj] = visited[ti][tj] + 1
        return 0

    print(f'#{T} {bfs(sp_x, sp_y, 16)}')