T = int(input())
for count_case in range(1, 1+T):
    N, M = map(int, input().split()) # N : 행렬크기, M : 찾아야 하는 단어길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로 행렬에서 이어지는 행렬이 1일때 count += 1, count값이 M(찾아야하는 단어의 길이)가 되면 result += 1
    # 만일 M이 되기전에 0이 한번이라도 나오면 count 초기화 하는 식
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == M:
                    result += 1
                count = 0
        if count == M:
            result += 1

    # 세로 행렬에서도 가로처럼 마찬가지로 진행
    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == M:
                    result += 1
                count = 0
        if count == M:
            result += 1

    print(f'#{count_case} {result}')