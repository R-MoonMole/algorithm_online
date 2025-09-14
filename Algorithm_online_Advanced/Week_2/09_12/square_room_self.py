import sys
sys.stdin = open('1861(2).txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)
    max_cnt = 0
    cnt = 0
    start = 0

    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if arr[ny][nx] == arr[y][x] + 1:
                    visited[arr[y][x]] = 1
                    break

    for i in range(1, len(visited)):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0

    print(f'#{tc} {start} {max_cnt + 1}')