T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    tree = []
    arr = [0]
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    result = []
    x = 0
    y = 0

    for i in range(1, N + 1):
        if 2 * i <= N:
            tree.append(i)
            tree.append(2 * i)
        if 2 * i + 1 <= N:
            tree.append(i)
            tree.append(2 * i + 1)

    for j in range(0, (N-1) * 2, 2):
        parent, child = tree[j], tree[j + 1]
        if L[parent] == 0:
            L[parent] = child
        else:
            R[parent] = child

    def tree_traverse(v):
        if v == 0:
            return
        tree_traverse(L[v])
        arr.append(v)
        tree_traverse(R[v])

    def inorder(v):
        if v > N:
            return
        inorder(v * 2)
        result.append([arr[v], v])
        inorder(v * 2 + 1)

    tree_traverse(1)
    inorder(1)

    for k in range(N):
        for l in range(1):
            if result[k][l] == 1:
                x = result[k][1]
            if result[k][l] == N//2:
                y = result[k][1]
    print(f'#{tc} {x} {y}')