T = int(input())
for count_case in range(1, 1+T):
    N, M = map(int, input().split()) # N : 행렬크기, M : 찾아야 하는 단어길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    real_count = 0


    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == M:
                    real_count += 1
                count = 0
        if count == M:
            real_count += 1

    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == M:
                    real_count += 1
                count = 0
        if count == M:
            real_count += 1

    print(f'#{count_case} {real_count}')