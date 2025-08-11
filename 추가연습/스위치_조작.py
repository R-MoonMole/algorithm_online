T = int(input())

for count_case in range(1, 1+T):

    N = int(input())
    arr_before = list(map(int, input().split()))
    arr_after = list(map(int, input().split()))
    count = 0

    for i in range(N):
        if arr_before[i] != arr_after[i]:
            count += 1
            for j in range(i, N):
                if arr_before[j] == 1:
                    arr_before[j] = 0
                elif arr_before[j] == 0:
                    arr_before[j] = 1

    print(f'#{count_case} {count}')