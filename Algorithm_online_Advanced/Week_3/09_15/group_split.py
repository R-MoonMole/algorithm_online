import sys
sys.stdin = open('11899.txt', 'r')

T = int(input())

def make_set(n):
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    return parents, ranks

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_y] < ranks[rep_x]:
        parents[rep_y] = rep_x
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = [arr[i:i+2] for i in range(0, len(arr), 2)]
    parents, ranks = make_set(N)
    cnt = 0

    for x, y in lst:
        union(x, y)

    for i in range(N+1):
        find_set(i)

    result = list(set(parents))

    print(f'#{tc} {len(result) - 1}')