T = int(input())

for count_case in range(1, T+1):
    N = int(input())
    arr = input()
    count = 0
    max_count = 0

    # 주어진 수열을 받아 반복문으로 하나씩 꺼내서 1일때 count증가, count가 최대일때 max_count 갱신
    # 0이 나오는 순간 count 초기화
    for i in arr:
        if i == '1':
            count += 1
            if max_count < count:
                max_count = count
        elif i == '0':
            count = 0

    print(f'#{count_case} {max_count}')
