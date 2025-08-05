'''
3
5
49679
5
08271
10
7797946543

'''
T = int(input()) # 테스트 케이스 input

count_case_number = 1 # 테스트 케이스번호를 위한 변수
for i in range(T):

    N = int(input())    # 카드 장수
    arr = list(map(int, input()))   # 주어지는 N개의 숫자
    max_number = 0      # 가장 많은 카드의 숫자
    max_number_count = 0    # 가장 많은 카드의 장수
    idx_searcher = 0    # 많은 카드 숫자의 idx를 찾기위한 searcher
    idx_list = [0] * 10    # 많은 카드 갯수를 정리할 빈 리스트


    for j in range(0, N):
        idx_list[arr[j]] += 1   # for 반복문 이용, idx_list에 0~9까지 사용된 횟수 순서대로 입력

    for k in range(0, 10):
        if idx_list[k] >= max_number_count:     # for, if 이용, 가장 많은 카드의 장수를 구함
            max_number_count = idx_list[k]

    # for, if 이용, 가장 많은 카드의 숫자(장수가 같을경우 적힌 숫자가 큰 쪽)을 구하기 위해
    # idx_list에서 index 0~9까지 반복하면서 리스트 요소가 초기값 0으로 설정된 idx_searcher보다
    # 크거나 같은값을 찾음(만일 같은값이면 높은수가 입력될 수 있도록)
        if idx_list[k] >= idx_searcher:
            idx_searcher = idx_list[k]
            max_number = k

    print(f'#{count_case_number} {max_number} {max_number_count}')
    count_case_number += 1





