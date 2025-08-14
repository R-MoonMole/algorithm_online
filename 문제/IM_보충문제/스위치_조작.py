T = int(input())

for count_case in range(1, 1+T):

    N = int(input())
    arr_before = list(map(int, input().split()))
    arr_after = list(map(int, input().split()))
    count = 0 # 얼마나 스위치를 껐다 켜야하는지 변수

    # 스위치 인덱스 0부터 시작, before, after을 비교하여 다르면 count를 1 올리는 동시에
    # before이 1이면 0으로, 0이면 1로, 그 인덱스부터 N까지 바꾸는걸 반복
    for i in range(N):
        if arr_before[i] != arr_after[i]:
            count += 1

            for j in range(i, N):
                if arr_before[j] == 1:
                    arr_before[j] = 0

                elif arr_before[j] == 0:
                    arr_before[j] = 1

    print(f'#{count_case} {count}')