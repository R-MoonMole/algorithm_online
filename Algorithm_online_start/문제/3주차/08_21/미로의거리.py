T = int(input())

for tc in range(1, 1+T):

    def start_point(N):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    return i, j

    def bfs(i, j, N):
        visited = [[0] * N for _ in range(N)]
        Q = []
        Q.append([i, j])
        visited[i][j] = 1

        while Q:
            ti, tj = Q.pop(0)
            if arr[ti][tj] == 3:
                return visited[ti][tj] - 2
            for di, dj in [[1,0], [0,-1], [-1,0], [0,1]]:
                wi, wj = ti+di, tj+dj
                if 0 <= wi < N and 0 <= wj < N and arr[wi][wj] != 1 and visited[wi][wj] == 0:
                    Q.append([wi, wj])
                    visited[wi][wj] = visited[ti][tj] + 1
        return 0

    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sti, stj = start_point(N)
    result = bfs(sti, stj, N)
    print(f'#{tc} {result}')