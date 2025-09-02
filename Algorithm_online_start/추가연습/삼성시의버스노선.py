T = int(input())

for count_case in range(1, 1+T):
    N = int(input())
    arr = [0] * 5001
    result = []

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            arr[i] += 1

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]

    for i in bus_stop:
        result.append(arr[i])

    print(f'#{count_case} ', end="")
    print(*result)