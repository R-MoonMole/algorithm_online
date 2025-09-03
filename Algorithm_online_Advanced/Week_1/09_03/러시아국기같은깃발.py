import sys
sys.stdin = open('sample_input_1.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    W = []
    B = []
    R = []

    min_cost = 10**10

    for i in arr:
        S = [M] * 3
        for j in range(M):
            if i[j] == 'W':
                S[0] -= 1
            elif i[j] == 'B':
                S[1] -= 1
            else:
                S[2] -= 1

        W.append(S[0])
        B.append(S[1])
        R.append(S[2])

    for j in range(0, N-2):
        for k in range(j+1, N-1):
            cost = 0

            cost += sum(W[:j+1])
            cost += sum(B[j+1:k+1])
            cost += sum(R[k+1:])
            if cost < min_cost:
                min_cost = cost

    print(f'#{tc} {min_cost}')
#
#     min_cost = float('inf')
#     print(W)
#     print(B)
#     print(R)
#     # i: 흰색 마지막 줄, j: 파란색 마지막 줄
#     for i in range(0, N - 2):
#         for j in range(i + 1, N - 1):
#             cost = 0
#             # 흰색 부분
#             cost += sum(W[:i + 1])
#             # 파란색 부분
#             cost += sum(B[i + 1:j + 1])
#             # 빨간색 부분
#             cost += sum(R[j + 1:])
#             min_cost = min(min_cost, cost)
#
#     print(f"#{tc} {min_cost}")