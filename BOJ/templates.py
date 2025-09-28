# DFS: 재귀 방식
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")  # 방문 확인용

    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)

# 예시 그래프 (인접 리스트)
graph = [
    [],        # 0번 노드 없음
    [2, 3],    # 1번 노드와 연결된 정점
    [1, 4, 5],
    [1],
    [2],
    [2]
]
visited = [False] * 6
dfs(graph, 1, visited)

# ====================================================================

from collections import deque

# BFS: 큐 방식
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=" ")

        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1],
    [2],
    [2]
]
visited = [False] * 6
bfs(graph, 1, visited)

# ====================================================================

# Kruskal MST
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = 4, 5
edges = [
    (1, 2, 1),
    (2, 3, 2),
    (3, 4, 3),
    (4, 1, 4),
    (1, 3, 5)
]  # (가중치, u, v)

edges.sort(key=lambda x: x[2])  # 가중치 기준 정렬
parent = [i for i in range(V+1)]

mst_cost = 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        mst_cost += w

print("MST 비용:", mst_cost)

# ====================================================================

import heapq

def prim(start, graph, V):
    visited = [False] * (V+1)
    q = [(0, start)]  # (비용, 노드)
    total = 0

    while q:
        cost, v = heapq.heappop(q)
        if visited[v]:
            continue
        visited[v] = True
        total += cost

        for nxt_cost, nxt in graph[v]:
            if not visited[nxt]:
                heapq.heappush(q, (nxt_cost, nxt))

    return total

V = 4
graph = [[] for _ in range(V+1)]
graph[1].append((1, 2))
graph[2].append((1, 1))
graph[2].append((2, 3))
graph[3].append((2, 2))
graph[3].append((3, 4))
graph[4].append((3, 3))

print("Prim MST 비용:", prim(1, graph, V))

# ====================================================================

import heapq

def dijkstra(start, graph, V):
    INF = 1e9
    dist = [INF] * (V+1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue

        for nxt_cost, nxt in graph[v]:
            cost = d + nxt_cost
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))

    return dist

V = 5
graph = [[] for _ in range(V+1)]
graph[1].append((2, 2))
graph[1].append((4, 3))
graph[2].append((1, 5))
graph[3].append((3, 4))
graph[4].append((2, 5))

print("최단거리:", dijkstra(1, graph, V))
