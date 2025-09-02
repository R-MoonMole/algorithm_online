'''
13 12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

V, E = map(int, input().split())
arr = list(map(int,input().split()))

L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

for i in range(0, E*2, 2):
    parent, child = arr[i], arr[i+1]
    if L[parent] == 0:
        L[parent] = child
    else:
        R[parent] = child

    P[child] = parent

def tree_traverse(v):
    if v == 0:
        return
    # 1. 처음 진입했을 때
    tree_traverse(L[v]) # 왼쪽
    # 2. 왼쪽 자식에서 돌아온 후
    print(v, end=" ")
    tree_traverse(R[v]) # 오른쪽
    # 3. 오른쪽 자식에서 돌아온 후


tree_traverse(1)
