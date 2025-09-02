T = int(input())

for case_number in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(M)]

    for i in arr:
        for k in range(M//2):
            if i[k] == i[-1-k]:
                pass


    for i in range(M):
        for j in range(N):
            if arr[i][j] == arr[i][N-j] and arr[i][j+1] == arr[i][N-1-j]:
                mt_list.append(arr[i][j])

    for k in range(N):
        for l in range(M-1):
            if arr[k][l] == arr[M-1-k][l] and arr[k+1][l] == arr[M-2-k][l]:
                print(arr[k][l])

    print(mt_list)



# def len(A):
#     k = 0
#     for i in A:
#         k += 1
#     return k
#
# def palindrome(B):
#     for i in range(1, len(B)/2):
#         if B[i] == B[len(B)-i]:
#             return B
#
#
#     for j in range(N):
#         for k in range(N):
#             if arr[j][k] == arr[j][N-1-k]:
#                     print(arr[j])


    #
    # print(arr)
    # for row in arr:
    #     print(*row)