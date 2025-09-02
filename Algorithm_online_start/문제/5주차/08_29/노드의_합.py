T = int(input())

for tc in range(1, 1+T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    count = 0

    for _ in range(M):
        arr = list(map(int, input().split()))

        for i in range(2):
            tree[arr[0]] = arr[1]

    def pre_order(n):
        global count
        if n <= N:
            count += tree[n]
            pre_order(n * 2)
            pre_order(n * 2 + 1)

    pre_order(L)
    print(f'#{tc} {count}')