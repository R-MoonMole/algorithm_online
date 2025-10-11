T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    if N > M:
        N, M = M, N
    if len(arr_1) > len(arr_2):
        M_arr = arr_1
        N_arr = arr_2
    else:
        M_arr = arr_2
        N_arr = arr_1

    result = 0
    for i in range(M-N+1):
        cnt = 0
        for j in range(N):
            cnt += N_arr[j] * M_arr[j+i]
        if cnt > result:
            result = cnt

    print(f'#{tc} {result}')