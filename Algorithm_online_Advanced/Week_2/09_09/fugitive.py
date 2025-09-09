dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

T = int(input())

for tc in range(1, 1+T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    def bfs(R, C):
        q = [(R, C)]
        visited[R][C] = 1

        while q:
            now_y, now_x = q.pop()
            dirs = types[arr[now_y][now_x]]





    bfs(R, C)