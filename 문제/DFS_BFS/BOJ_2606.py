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
        if visited[i] == 0:
            DFS(i)
            result.append(i)

DFS(1)

print(len(result))

# dfs 순서
#
# dfs 함수에 들어가는걸 정함 -> v (여러개가 들어갈 수도 있음)
# visited[v] -> 1로 설정 (방문했다는 뜻)
# arr[v](여기선 graph[v])를 반복해서 꺼낸 값(i)이 visited에 들어갔을때 0인경우(방문하지 않은 곳일 경우)
# i에 대해 재귀, 결과를 result에 append