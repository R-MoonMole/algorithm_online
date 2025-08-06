'''
3
3 5
2 1 1 2 2
2 2 1 2 2
2 2 1 1 2
5 5
3 4 1 2 3
3 4 1 3 2
2 3 2 4 1
1 4 4 1 3
2 2 3 4 4
5 8
1 3 4 4 4 4 3 3
4 1 2 4 3 1 4 4
4 1 4 4 1 4 2 1
3 2 4 2 1 1 2 1
4 4 1 4 4 2 2 2

'''

dr = [0, 1, 0, -1] # 기준점 기준 십자모양의 풍선을 구하기 위한 변수
dc = [1, 0, -1, 0]

T = int(input()) # 테스트 케이스 input
count_case_number = 1 # 테스트 케이스 번호 출력을 위한 변수

for _ in range(T): # 주어진 테스트 케이스만큼 반복

    N, M = map(int, input().split()) # 격자판의 행 열 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # 주어진 행렬 넣을 변수
    paper_pollen = 0 # 종이 꽃가루 입력을 위한 변수
    max_paper_pollen = 0 # 최대 종이 꽃가루 수 변수

    for r1 in range(0, N, 1): # 기준점을 설정하는 변수
        for c1 in range(0, M, 1):
            paper_pollen = 0 # 반복때 마다 종이 꽃가루 초기화
            paper_pollen += arr[r1][c1] # 기준점의 꽃가루 수 할당

            for dir in range(4): # 상하좌우 네 방향을 반복할 반복문(4방향이라 범위 4)
                for i in range(1, 2): # 방향으로 몇칸이 더 터질지 설정(여기선 1칸)
                    nr = r1 + dr[dir] * i # 기준점 기준 행렬을 이동하여 상하좌우 변수 출력
                    nc = c1 + dc[dir] * i
                    if 0 <= nr < N and 0 <= nc < M: # 혹시나 배열 밖으로 벗어나지 않게 설정
                        paper_pollen += arr[nr][nc] # 상하좌우의 값을 종이꽃가루 변수에 더함
            if max_paper_pollen < paper_pollen: # 최대 종이 꽃가루 변수에 넣기위한 과정
                max_paper_pollen = paper_pollen # 기준점과 상하좌우를 더했을 때 max_paper_poller보다 크면 최댓값이므로 그대로 할당

    print(f'#{count_case_number} {max_paper_pollen}') # 출력
    count_case_number += 1