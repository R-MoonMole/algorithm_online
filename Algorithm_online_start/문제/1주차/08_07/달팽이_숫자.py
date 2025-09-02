'''
2
3
4

'''
dr = [0, 1, 0, -1] # 우 하 좌 상 순서대로
dc = [1, 0, -1, 0]

T = int(input()) # 테스트 케이스 개수 T값 입력받음

for count_case_number in range(1, 1+T): # 테스트 케이스 갯수만큼 반복문 진행

    N = int(input()) # 배열의 크기
    arr = [[0]*N for _ in range(N)] # 0으로 채워진 빈 배열 생성
    r, c = 0, 0 # 처음 출발하는 좌표
    number = 1 # 1씩 증가하는 값을 표현하기 위해 만든 변수
    dir = 0 # 방향을 설정하는 변수로 0이면 우, 1이면 하, 2면 좌, 3이면 상 방향으로 움직이게 됨

    for i in range(N**2): # 반복문은 NxN행렬을 채워야하므로 N^2번 반복
        arr[r][c] = number # 초기 좌표에 number 입력 및 number에 1을 더함
        number += 1

        new_r = r + dr[dir] # 우측으로(dir이 0이므로) 한칸 옮겼을때의 행 좌표를 받음
        new_c = c + dc[dir] # 우측으로(dir이 0이므로) 한칸 옮겼을때의 열 좌표를 받음

        # new_r과 new_c의 좌표가 NxN행렬을 벗어나거나, 그 좌표에 이미 0값이 아닌 다른 값이 들어가있을때를 판단
        if (not(0 <= new_r < N and 0 <= new_c < N)) or arr[new_r][new_c] != 0:
            dir = (dir + 1) % 4 # 위의 조건을 만족하면 방향 dir을 0(우측)에서 1(아래)로 바꿔줌(4로나눈 나머지가 순환되는것을 이용)
            new_r = r + dr[dir] # 좌표를 다시 변경해줌
            new_c = c + dc[dir]

        r = new_r # 변경한 좌표를 반복문 안에있는 기준 좌표에다가 넣어줌
        c = new_c

    print(f'#{count_case_number}') # 출력
    for row in arr:
        print(*row)