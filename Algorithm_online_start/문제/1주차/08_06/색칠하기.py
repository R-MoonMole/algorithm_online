'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

'''

T = int(input()) # 테스트 케이스 입력
count_case_number = 1 # 테스트 케이스 번호 입력용 변수

for _ in range(T):

    emt = 10 # 초기 배열의 행,열 값
    arr = [[0] * emt for _ in range(emt)] # 요소가 0인 초기 배열 변수
    coloring_number = int(input()) # 색 칠하는 횟수 변수
    purple = 0 # 초기 보라색의 갯수 변수

    for _ in range(coloring_number): # 색 칠하는 횟수만큼 반복해서 변수를 담는다
        r1, c1, r2, c2, color = map(int, input().split())
        # 왼쪽위 모서리 인덱스 r1, c1와 오른쪽 아래 모서리 r2, c2와 색상정보 color(빨강 : 1, 파랑 : 2)를 담기위한 변수

        for r in range(r1, r2+1): # r1부터 r2+1까지 반복 (행)
            for c in range(c1, c2+1): # c1부터 c2+1까지 반복 (열)
                arr[r][c] += color # 색을 칠한다(빨간색의 위치가 안겹치니까 if 굳이 필요 없음)

    for i in arr: # 위에서 색칠하고 얻은 배열에서 보라색 (3)을 찾기위한 반복문
        for j in i:
            if j == 3:
                purple += 1 # arr 배열에서 3(보라색)이 나올때마다 초기에 설정한 purple변수에 1을 더함

    print(f'#{count_case_number} {purple}')
    count_case_number +=1