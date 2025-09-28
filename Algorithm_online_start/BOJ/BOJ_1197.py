import heapq

V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    adj[a].append((w, b))
    adj[b].append((w, a))

visited = [False] * (V + 1)
hq = []                      # (가중치, 정점)
heapq.heappush(hq, (0, 1))   # 임의 시작 정점 1에서 시작
mst_cost = 0
picked = 0

while hq and picked < V:
    w, v = heapq.heappop(hq)
    if visited[v]:
        continue
    visited[v] = True
    mst_cost += w
    picked += 1

    for nw, nv in adj[v]:
        if not visited[nv]:
            heapq.heappush(hq, (nw, nv))

print(mst_cost)