T = int(input())

for count_case in range(1, 1+T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
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