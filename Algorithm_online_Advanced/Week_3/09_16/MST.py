import sys
sys.stdin = open('11900.txt', 'r')

T = int(input())

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])

    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

for tc in range(1, 1+T):
    V, E = map(int, input().split())
    edges = []

    for _ in range(E):
        u, v, weight = map(int, input().split())
        edges.append((u, v, weight))

    edges.sort(key=lambda x: x[2])

    parents = [i for i in range(V + 1)]
    cnt = 0
    result = 0

    for u, v, weight in edges:

        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            result += weight

            if cnt == V:
                break

    print(f'#{tc} {result}')