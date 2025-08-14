T = int(input())

for count_case in range(1, 1+T):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0

    for i in range(N):
        length = 0
        for j in range(M):
            if arr[i][j] == 1:
                length += 1
                if length >= 2 and max_length < length:
                    max_length = length
            else:
                length = 0

    for j in range(M):
        length = 0
        for i in range(N):
            if arr[i][j] == 1:
                length += 1
                if length >= 2 and max_length < length:
                    max_length = length
            else:
                length = 0

    print(f'#{count_case} {max_length}')