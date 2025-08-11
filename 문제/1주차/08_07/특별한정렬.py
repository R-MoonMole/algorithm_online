'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

'''

T = int(input()) # 테스트 케이스 개수 T 입력

for count_case_number in range(1, T+1): # 테스트 케이스만큼 반복, 테스트케이스 번호 출력에도 사용
    N = int(input()) # 정수의 개수 N 입력
    case_list = list(map(int, input().split())) # 주어지는 정수를 리스트로 받음
    result = [[] for _ in range(10)] # 후에 10개만 출력하기 위한 빈 리스트

    for j in range(N):

        for k in range(j, N): # 반복문 이용, j가 짝수일때 큰수가 앞으로, j가 홀수일때 작은수가 앞으로 오도록 반복
            min_idx = k
            max_idx = k
            if j % 2 != 0:
                if case_list[min_idx] > case_list[j]:
                    min_idx = j
                case_list[j], case_list[min_idx] = case_list[min_idx], case_list[j]

            if j % 2 == 0:
                if case_list[max_idx] < case_list[j]:
                    max_idx = j
                case_list[j], case_list[max_idx] = case_list[max_idx], case_list[j]

    for l in range(10): # 나오고 정렬된 숫자를 앞에 10자리까지만 출력하기 위한 처리과정
        result[l] = case_list[l]

    print(f'#{count_case_number}', end=" ")
    print(*result)