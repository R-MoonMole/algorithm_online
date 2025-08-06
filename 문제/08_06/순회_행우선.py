'''
3
3 4 3
5 5 1
2 3 4

'''

T = int(input()) # 테스트 케이스 갯수 입력
count_case_number = 1 # 테스트케이스 번호 출력용

for _ in range(T):

    emt = 10 # 배열의 크기 값
    arr = [[0] * emt for _ in range(emt)] # 초기값이 0으로 채워진 빈 배열 만들어 변수에 입력
    result = 1 # 첫 좌상단 모서리에 들어갈 숫자
    R, C, N = map(int, input().split()) # 좌상단의 행 R, 열 C, 크기 N 변수

    for i in range(R, R+N): # 주어진 좌상단의 행 R부터 크기 N을 더한 R+N까지를 range로하여 반복
        for j in range(C, C+N): # 주어진 좌상단의 열 C부터 크기 N을 더한 C+N까지를 range로하여 반복
            arr[i][j] = result # arr의 행렬에 result를 입력 후 그다음 입력을 위해 result에 1을 더함
            result += 1

    print(f'#{count_case_number}') # 테스트케이스 번호 출력
    count_case_number += 1 # 테스트 케이스 번호에 1더함
    for row in arr: # 출력 모양을 맞추기 위해 반복문 사용
        print(*row)


