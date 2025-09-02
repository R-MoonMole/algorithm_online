for _ in range(10): # 테스트 케이스만큼 반복하기 위한 반복문

    count_case_number = int(input()) # 처음에 주어지는 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)] # 그다음 주어지는 10000개의 수를 100X100 배열로
    sum_diag1 = 0 # 오른쪽 아래 대각선 합
    sum_diag2 = 0 # 왼쪽 아래 대각선 합
    sum_r = 0 # 행 값 더한 값
    max_sum_r = 0 # 행 값 더한 값 중에 최고값
    sum_c = 0 # 열 값 더한 값 변수
    max_sum_c = 0 # 열 값 더한 값 중에 최고값

    for i in range(100): # 오른쪽 아래 대각선 합을 구하기 위한 반복문
        sum_diag1 += arr[i][i]

    for j in range(100): # 왼쪽 아래 대각선 합을 구하기 위한 반복문
        sum_diag2 += arr[j][99-j]

    for k in range(100): # 행 값 더한 값을 구하기 위한 반복문
        sum_r = 0
        for l in range(100):
            sum_r += arr[k][l]
            if max_sum_r < sum_r:
                max_sum_r = sum_r

    for n in range(100): # 열 값 더한 값을 구하기 위한 반복문
        sum_c = 0
        for m in range(100):
            sum_c += arr[m][n]
            if max_sum_c < sum_c:
                max_sum_c = sum_c

    # 조건문을 사용, 구한 값 크기를 비교, 가장 큰 값 출력
    if sum_diag1 >= sum_diag2 and sum_diag1 >= max_sum_r and sum_diag1 >= max_sum_c:
        print(f'#{count_case_number} {sum_diag1}')

    elif sum_diag2 >= sum_diag1 and sum_diag2 >= max_sum_r and sum_diag2 >= max_sum_c:
        print(f'#{count_case_number} {sum_diag2}')

    elif max_sum_c >= sum_diag2 and max_sum_c >= max_sum_r and max_sum_c >= sum_diag1:
        print(f'#{count_case_number} {max_sum_c}')

    elif max_sum_r >= sum_diag2 and max_sum_r >= sum_diag1 and max_sum_r >= max_sum_c:
        print(f'#{count_case_number} {max_sum_r}')