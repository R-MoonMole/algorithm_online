T = int(input())

for count_case in range(1, 1+T):

    N, Q = map(int, input().split())
    arr = [0] * (N+1)
    result = []

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i+1

    for k in range(1, N+1):
        result.append(arr[k])

    print(f'#{count_case} ', end="")
    print(*result)
