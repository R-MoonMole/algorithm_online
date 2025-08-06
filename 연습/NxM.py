N = 5
M = 4
# 0으로 채워진 NxN 배열생성
arr = [[0]*M for _ in range(N)]

# # 행 우선 순회
# cnt = 1
# for i in range(N):
#     for j in range(M):
#         arr[i][j] = cnt
#         cnt += 1

# 열 우선 순회
cnt = 1
for i in range(N):
    for j in range(M):
        arr[i][j] = cnt
        cnt += 1

# # 지그재그 우선 순회
# cnt = 1
# for i in range(N):
#     if i % 2 == 0:
#         for j in range(M):
#             arr[i][j] = cnt
#             cnt += 1
#     else:
#         for j in range(M-1, -1, -1):
#             arr[i][j] = cnt
#             cnt += 1


for row in arr:
    print(*row)