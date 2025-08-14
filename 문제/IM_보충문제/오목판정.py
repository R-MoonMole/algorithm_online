T = int(input())
dr = [-1, 1, 1, -1] # 우상부터 시계방향순
dc = [1, 1, -1, -1]

for count_case in range(1, 1+T):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = 'NO'

# 가로에서 o가 5개연속으로 있는지 확인
    for i in range(N):
        correct = 0
        for j in range(N):
            if arr[i][j] == 'o':
                correct += 1
            elif arr[i][j] == '.':
                correct = 0
            if correct == 5:
                result = 'YES'
                correct = 0
                break

# 세로에서 o가 5개연속으로 있는지 확인
    for i in range(N):
        correct = 0
        for j in range(N):
            if arr[j][i] == 'o':
                correct += 1
            elif arr[j][i] == '.':
                correct = 0
            if correct == 5:
                result = 'YES'
                break

# 대각선에서 o가 5개연속으로 있는지 확인 기준점이 o일경우에만 작동, 그 이후 대각 한 방향으로 4개가 연속 있는지 확인
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    correct = 0
                    for l in range(1, 5):
                        nr = i + dr[k] * l
                        nc = j + dc[k] * l
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                correct += 1
                            elif arr[nr][nc] == '.':
                                correct = 0
                                break
                            if correct == 4:
                                result = 'YES'

    print(f'#{count_case} {result}')