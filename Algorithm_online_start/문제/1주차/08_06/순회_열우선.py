'''
3
3 4 3 4
5 2 1 5
2 3 4 6

'''

T = int(input()) # 테스트 케이스 갯수 입력
count_case_number = 1 # 테스트케이스 번호 출력용

for _ in range(T):

    emt = 10 # 배열의 크기 값
    arr = [[0] * emt for _ in range(emt)] # 초기값이 0으로 채워진 빈 배열 만들어 변수에 입력
    R, C, W, H = map(int, input().split()) # 좌상단의 행 R, 열 C, 너비 W, 높이 H 변수
    result = 1 # 첫 좌상단 모서리에 들어갈 숫자

    for i in range(C, C+W): # 열을 먼저 출력하기위해 열을 반복문에 집어넣음 (열부터 열+너비)까지
        for j in range(R, R+H): # 행을 출력하기위해 행을 반복문에 집어넣음 (행부터 행+높이)까지
            arr[j][i] = result
            result += 1

    print(f'#{count_case_number}')
    count_case_number += 1
    for row in arr:
        print(*row)