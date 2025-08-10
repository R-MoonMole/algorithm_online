T = int(input())

for count_case in range(1, 1+T):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    in_squ = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        row_sum = 0
        for j in range(1, N+1):
            row_sum += out_squ[i-1][j-1]
            in_squ[i][j] = in_squ[i-1][j] + row_sum

    ans = []
    for _ in range(M):
        r, c, A = map(int, input().split())

        r1, c1 = r-1, c-1
        r2, c2 = r + A-1, c + A-1
        s = in_squ[r2][c2] - in_squ[r1][c2] - in_squ[r2][c1] + in_squ[r1][c1]
        ans.append(s)

    print(f"#{count_case}", *ans)