T = int(input())
for tc in range(1, 1+T):

    def bfs(S, G, V, arr):
        visited = [0] * (V + 1)
        Q = [S]
        visited[S] = 1

        while Q:
            t = Q.pop(0)
            if t == G:
                return visited[t] - 1
            for w in arr[t]:
                if visited[w] == 0:
                    visited[w] = visited[t] + 1
                    Q.append(w)
        return 0

    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        arr[v1].append(v2)
        arr[v2].append(v1)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G, V, arr)}')