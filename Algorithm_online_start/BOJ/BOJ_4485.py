import sys
sys.stdin = open('4485.txt', 'r')

import heapq

def dijkstra(arr, N):
    INF = 10**9
    dist = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dist[0][0] = arr[0][0]

    for _ in range(N*N):
        min_cost = INF
        y, x = -1, -1
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and dist[i][j] < min_cost:
                    min_cost = dist[i][j]
                    y, x = i, j
        if y == -1:
            break

        visited[y][x] = 1
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if dist[y][x] + arr[ny][nx] < dist[ny][nx]:
                    dist[ny][nx] = dist[y][x] + arr[ny][nx]

    return dist[N - 1][N - 1]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
testcase = 0
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    testcase += 1

    result = dijkstra(arr, N)
    print(f'Problem {testcase}: {result}')




