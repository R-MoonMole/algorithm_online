T = int(input())
dr = [0, 1, 0, -1] # 우하좌상 순서
dc = [1, 0, -1, 0]

for count_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_boom = 0 # 풍선이 터지는 최대 점수를 담을 변수

    for i in range(N):
        for j in range(N):
            boom = 0 # 풍선 터지는 값 담을 변수 초기화
            boom = arr[i][j] # 기준점에 있는 점수를 담음
            for k in range(4):
                for l in range(1, N):
                    nr = i + dr[k] * l
                    nc = j + dc[k] * l
                    if 0 <= nr < N and 0 <= nc < N:
                        boom += arr[nr][nc]
                        if max_boom < boom:
                            max_boom = boom

    print(f'#{count_case} {max_boom}')