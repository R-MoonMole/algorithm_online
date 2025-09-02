T = int(input())

for count_case in range(1, 1+T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0:
                arr[i][j] = 1
            elif i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{count_case}')
    for row in arr:
        for x in row:
            if x:
                print(x, end=' ')
        print()