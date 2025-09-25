# BOJ_7569 : 토마토마토
# https://www.acmicpc.net/problem/7569
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def recur():
    q = deque()
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x] + 1
                q.append((ny, nx))

    result = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 0:
                print(-1)
                return
            result = max(result, arr[y][x])
    print(result - 1)

recur()