# T = int(input())
# for tc in range(1, T+1):
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))
#     L = [0] * (E+2)
#     R = [0] * (E+2)
#
#     count = 0
#
#     for i in range(0, E*2, 2):
#         parent, child = arr[i], arr[i + 1]
#         if L[parent] == 0:
#             L[parent] = child
#         else:
#             R[parent] = child
#
#     def tree_traverse(v):
#         global count
#
#         if v == 0:
#             return
#         tree_traverse(L[v])
#         count += 1
#         tree_traverse(R[v])
#
#     tree_traverse(N)
#     print(f'#{tc} {count}')


def pre_order(T):
    if T == 0:  # 존재하지 않는 정점이면
        return 0
    l = pre_order(left[T])  # pre_order(T.left)
    r = pre_order(right[T])
    return l + r + 1


E, N = map(int, input().split())
arr = list(map(int, input().split()))
V = E + 1       #마지막 정점 번후
left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

print(pre_order(N))
