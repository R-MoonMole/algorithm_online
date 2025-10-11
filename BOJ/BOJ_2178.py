from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * (M) for _ in range(N)]
visited[0][0] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def recur():
    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and visited[ny][nx] == 0:
                arr[ny][nx] = arr[y][x] + 1
                q.append((ny, nx))
                visited[ny][nx] = 1

    print(arr[N-1][M-1])

recur()
