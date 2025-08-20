arr = ['A', 'B', 'C', 'D']
N = len(arr)

# for i in range(0, N):
#     arr[0], arr[i] = arr[i] , arr[0]
#     # ------------------ 첫번째 상태
#     for j in range(1, N):
#         arr[1], arr[j] = arr[j], arr[1]
#         # ------------------ 두번째 상태
#         for k in range(2, N):
#             arr[2], arr[k] = arr[k], arr[2]
#             print(*arr)
#             arr[2], arr[k] = arr[k], arr[2]
#         # ------------------
#         arr[1], arr[j] = arr[j], arr[1]
#     # ------------------
#     arr[0], arr[i] = arr[i], arr[0]
#

# 이걸 재귀로 변경

def backtrack(k):
    if k == N:
        print(*arr)
    else:

        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            # ------------------
            # 재귀호출
            backtrack(k + 1)
            # ------------------
            arr[k], arr[i] = arr[i], arr[k]

backtrack(0)