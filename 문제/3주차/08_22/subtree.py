T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    L = [0] * (E+2)
    R = [0] * (E+2)

    count = 0

    for i in range(0, E*2, 2):
        parent, child = arr[i], arr[i + 1]
        if L[parent] == 0:
            L[parent] = child
        else:
            R[parent] = child

    def tree_traverse(v):
        global count

        if v == 0:
            return
        tree_traverse(L[v])
        count += 1
        tree_traverse(R[v])

    tree_traverse(N)
    print(f'#{tc} {count}')