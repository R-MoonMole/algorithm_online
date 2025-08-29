# BOJ_2606 : 바이러스
# https://www.acmicpc.net/problem/2606

N = int(input())
C = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []

for _ in range(C):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
            result.append(i)

DFS(1)

print(len(result))