T = int(input())
dr = [0, 1, 0, -1] # 우하좌상
dc = [1, 0, -1, 0]

for count_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    x, y = 0, 0 # 몬스터 좌표
    count = 0 # 벽, 광선을 제외한 0을 체크하기위한 변수

    # 괴물의 좌표를 구하기 위한 반복문
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j

    # 괴물 좌표 기준으로 우하좌상순으로 빔을 쏨, 벽(1)에 맞으면 break, 아니면 행렬을 벗어나지않는 선에서 N길이까지 광선을 쏨
    for k in range(4):
        for l in range(1, N):
            nr = x + dr[k]*l
            nc = y + dc[k]*l
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1
                else:
                    break

    # 광선과 벽을 제외한 0의 갯수를 체크하는 반복문
    for w in range(N):
        for e in range(N):
            if arr[w][e] == 0:
                count += 1

    print(f'#{count_case} {count}')