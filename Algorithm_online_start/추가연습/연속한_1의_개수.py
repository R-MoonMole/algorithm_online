T = int(input()) # 테스트 케이스 입력

for count_case in range(1, 1+T): # 테스트 케이스만큼 반복

    N = int(input()) # 수열 길이 N 변수
    arr = list(input()) # 수열 리스트 변수
    one_counter = 0 # 1을 셀 변수
    zero_counter = 0 # 0을 셀 변수
    max_one_counter = 0 # 최대 연속되는 1의 개수 변수

    for i in range(N):
        if arr[i] == '0': # i가 0이면 zero_counter 1증가
            zero_counter += 1
        elif arr[i] == '1': # i가 1일때
            if zero_counter == 0: # zero_counter가 0이면 그냥 1증가
                one_counter += 1
                if max_one_counter < one_counter: # max_one_counter보다 크면 max_one_counter에 입력
                    max_one_counter = one_counter
            elif zero_counter > 0: # zero_counter가 0보다 크면(0이 이전에 나왔으면)
                one_counter = 0 # zero_counter, one_counter 초기화하고 one_counter 1 증가
                zero_counter = 0
                one_counter += 1
                if max_one_counter < one_counter: # max_one_counter보다 크면 max_one_counter에 입력
                    max_one_counter = one_counter

    print(f'#{count_case} {max_one_counter}') # 출력
