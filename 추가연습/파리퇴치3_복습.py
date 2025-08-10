T = int(input())
cro_dr = [0, 1, 0, -1]
cro_dc = [1, 0, -1, 0]
dia_dr = [-1, 1, 1, -1]
dia_dc = [1, 1, -1, -1]

for count_case in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def spray_sum(r, c, dr, dc):
        S = arr[r][c]
        for i in range(4):
            for j in range(1, M):
                nr = r+dr[i] * j
                nc = c+dc[i] * j
                if 0 <= nr < N and 0 <= nc < N:
                    S += arr[nr][nc]
                else:
                    break
        return S

    max_kill = 0
    for k in range(N):
        for l in range(N):
            cro_sum = spray_sum(k, l, cro_dr, cro_dc)
            dia_sum = spray_sum(k, l, dia_dr, dia_dc)
            if max_kill < cro_sum:
                max_kill = cro_sum
            elif max_kill < dia_sum:
                max_kill = dia_sum

    print(f'#{count_case} {max_kill}')