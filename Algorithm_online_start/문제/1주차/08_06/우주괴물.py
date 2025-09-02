'''
1
5
0 0 0 1 0
1 0 1 1 0
0 0 1 0 2
1 0 0 0 0
1 1 1 1 0

'''
dr = [0, 1, 0, -1] # 광선을 상하좌우로 쏘기위한 방향 변수 설정
dc = [1, 0, -1, 0]

T = int(input()) # 테스트 케이스 개수 input

for count_case_number in range(1, T+1): # 테스트 케이스 횟수만큼 반복

    N = int(input()) # 배열 행 열 크기 변수
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열 input 및 생성
    r = 0 # 괴물이 있는 행
    c = 0 # 괴물이 있는 열
    empty_space = 0 # 빈 칸의 개수를 세기위한 변수

    for i in range(N): # 괴물의 위치를 찾기 위한 반복문
        for j in range(N):
            if arr[i][j] == 2:
                r = i
                c = j

    for dir in range(4):
        for k in range(1, N):
            nr = r + dr[dir] * k
            nc = c + dc[dir] * k
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1
                else:
                    break

    for l in arr:
        for row in l:
            if row == 0:
                empty_space += 1

    print(f'#{count_case_number} {empty_space}')