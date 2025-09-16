import sys
sys.stdin = open('11901.txt', 'r')

from heapq import heappush, heappop

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dist = [[21e9] * N for _ in range(N)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while pq:
        cost, y, x = heappop(pq)

        if (y, x) == (N-1, N-1):
            break

        if cost > dist[y][x]:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                extra = 0
                if arr[ny][nx] > arr[y][x]:
                    extra = arr[ny][nx] - arr[y][x]
                new_cost = cost + 1 + extra

                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heappush(pq, (new_cost, ny, nx))

    result = dist[N-1][N-1]
    print(f'#{tc} {result}')