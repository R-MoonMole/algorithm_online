T = int(input())

for count_case in range(1, 1+T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b) # 유향그래프라 이것만.

    Start, Goal = map(int, input().split())
    S = []
    visited = [0] * (V + 1)
    v = Start
    S.append(v)
    visited[v] = 1
    result = 0

    while S:

        for w in arr[v]:

            if not visited[w]:
                S.append(v)
                visited[w] = 1
                v = w
                break

        else:

            if v == Goal:
                result = 1
                break

            v = S.pop()

    print(f'#{count_case} {result}')

# def DFS(v) # v: 방문하는 정점
#     visited[v] = 1
#     for w in G[v]:
#         if not visited[w]:
#             DFS(w)
# DFS(start)
# print(visited[end])