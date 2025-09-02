T = int(input()) # 테스트 케이스 T를 입력
# 십자모양(우하좌상 순서)의 배열 위치
cro_dr = [0, 1, 0, -1]
cro_dc = [1, 0, -1, 0]
# 대각모양(1시, 5시, 7시, 11시 순서)의 배열 위치
dia_dr = [-1, 1, 1, -1]
dia_dc = [1, 1, -1, -1]

# 테스트 케이스만큼 반복, N, M 변수 등록, arr 배열에 행렬을 입력 받음
for count_case in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    # 함수 spray_sum을 만듬(행, 열, 델타 행, 델타 열)
    def spray_sum(r, c, dr, dc):
        S = arr[r][c] # 행렬의 중간값도 S에 넣어서 포함하기 위함
        for i in range(4): # 4방향(상하좌우, 대각4방향)을 구하기 위한 반복
            for j in range(1, M): # M의 세기로 스프레이를 분사
                nr = r+dr[i] * j # r에 dr방향으로 j만큼 분사
                nc = c+dc[i] * j # c에 dc방향으로 j만큼 분사
                if 0 <= nr < N and 0 <= nc < N: # 분사하는 곳이 행렬을 벗어나지 않으면 S에 더함
                    S += arr[nr][nc]
                else: # 벗어나면 break (그 순간의 방향 j만 break가 설정됨)
                    break
        return S

    max_fly_kill = 0 # 파리를 잡는 최댓값의 초기값을 설정
    for k in range(N):
        for l in range(N):
            cro_sum = spray_sum(k, l, cro_dr, cro_dc) # 함수를 이용, 십자모양의 파리잡는 수 체크
            dia_sum = spray_sum(k, l, dia_dr, dia_dc) # 대각모양 파리잡는수 체크
            if cro_sum > max_fly_kill: # 둘중에 큰 값을 찾아서 max_fly_kill에 넣음
                max_fly_kill = cro_sum
            if dia_sum > max_fly_kill:
                max_fly_kill = dia_sum

    print(f'#{count_case} {max_fly_kill}')
