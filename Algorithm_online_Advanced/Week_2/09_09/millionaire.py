T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    check = 0
    result = 0
    arr = arr[::-1]

    for i in range(N):
        if arr[i] >= check:
            check = arr[i]

        elif arr[i] < check:
            result += (check - arr[i])

    print(f'#{tc} {result}')