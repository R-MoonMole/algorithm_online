T = int(input())

for count_case in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(1, j+1):
            if 0 <= i-k-1 and i+k-1 < N:
                if arr[i-k-1] == arr[i+k-1]:
                    if arr[i-k-1] == 1:
                        arr[i-k-1], arr[i+k-1] = 0, 0
                    elif arr[i-k-1] == 0:
                        arr[i-k-1], arr[i+k-1] = 1, 1
            else:
                break

    print(f'#{count_case}', *arr)