T = int(input())

for count_case in range(1, 1+T):
    N, M = map(int, input().split()) # N : 돌의 수, M : 뒤집기 횟수
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split()) # i, j : i번째 돌을 사이에 두고 마주보는 j개의 돌, 같은색 : 뒤집, 다른색 : 유지

        # i번을 두고 i-k, i+k인 돌이 0과 N의 범위 안에 있을때(out of range방지)같을경우
        for k in range(1, j+1):
            if 0 <= i-k-1 and i+k-1 < N:
                if arr[i-k-1] == arr[i+k-1]: # 같을경우 1이면 0으로, 0이면 1로

                    if arr[i-k-1] == 1:
                        arr[i-k-1], arr[i+k-1] = 0, 0

                    elif arr[i-k-1] == 0:
                        arr[i-k-1], arr[i+k-1] = 1, 1
            else:
                break # 이외에는 break

    print(f'#{count_case}', *arr)