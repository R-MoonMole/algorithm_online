T = int(input())
crs_dr = [0, 1, 0, -1]
crs_dc = [1, 0, -1, 0]
dia_dr = [-1, 1, 1, -1]
dia_dc = [1, 1, -1, -1]

for count_case in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def spray_sum(r, c, dr, dc):
        S = arr[r][c]
        for i in range(4):
            for j in range(1, M):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if 0 <= nr < N and 0 <= nc < N:
                    S += arr[nr][nc]
                else:
                    break
        return S

    max_kill_fly = 0
    for k in range(N):
        for l in range(N):
            crs_sum = spray_sum(k, l, crs_dr, crs_dc)
            dia_sum = spray_sum(k, l, dia_dr, dia_dc)
            if crs_sum > max_kill_fly:
                max_kill_fly = crs_sum
            elif dia_sum > max_kill_fly:
                max_kill_fly = dia_sum

    print(f'#{count_case} {max_kill_fly}')