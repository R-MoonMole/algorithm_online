N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")
    for next in graph[v]:
        if not visited[next]:
            dfs(next, visited)



