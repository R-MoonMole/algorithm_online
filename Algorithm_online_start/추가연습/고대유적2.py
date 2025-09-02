data_number = int(input())

for count_case in range(1, 1+data_number):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    long_length = 0

    for i in range(N):
        length = 0
        for j in range(M):
            if arr[i][j] == 1:
                length += 1

                if length >= 2 and long_length < length:
                    long_length = length

            else:
                length = 0

    for j in range(M):
        length = 0
        for i in range(N):
            if arr[i][j] == 1:
                length += 1

                if length >= 2 and long_length < length:
                    long_length = length

            else:
                length = 0

    print(f'#{count_case} {long_length}')