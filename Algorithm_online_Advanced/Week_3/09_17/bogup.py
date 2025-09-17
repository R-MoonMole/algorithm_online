dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    MAP = [list(map(int, input())) for _ in range(N)]

    D = [[1e6] * N for _ in range(N)]
    D[0][0] = MAP[0][0]
    Q = [(0, 0)]

    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if D[nr][nc] > D[r][c] + MAP[nr][nc]:
                D[nr][nc] = D[r][c] + MAP[nr][nc]
                Q.append((nr, nc))
    print(f'#{tc} {D[N-1][N-1]}')