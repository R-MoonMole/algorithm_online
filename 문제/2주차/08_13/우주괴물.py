T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for count_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    x, y = 0, 0
    count = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j

    for k in range(4):
        for l in range(1, N):
            nr = x + dr[k]*l
            nc = y + dc[k]*l
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1
                else:
                    break

    for w in range(N):
        for e in range(N):
            if arr[w][e] == 0:
                count += 1

    print(f'#{count_case} {count}')