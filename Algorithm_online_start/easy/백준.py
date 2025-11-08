import sys
sys.stdin = open('asdf.txt', 'r')

from collections import deque

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

INF = 10**9
best_sum = INF
best_person = 1

for i in range(1, N + 1):
    dist = [-1] * (N + 1)
    dist[i] = 0
    q = deque([i])

    while q:
        cur = q.popleft()
        for next in lst[cur]:
            if dist[next] == -1:
                dist[next] = dist[cur] + 1
                q.append(next)

    total = sum(d for d in dist[1:] if d != -1)

    if total < best_sum:
        best_sum = total
        best_person = i

print(best_person)