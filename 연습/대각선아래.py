N = 6
# 0으로 채워진 NxN 배열생성
arr = [[0]*N for _ in range(N)]

# 대각선 포함 아래
for i in range(N):
    for j in range(N):
        if j <= i:
            arr[i][j] = 1

# 대각선 포함 아래2
for i in range(N):
    for j in range(0, i+1):
        arr[i][j] = 1


# 대각선 포함 위
for i in range(N):
    for j in range(N):
        if j >= i:
            arr[i][j] = 1

# 대각선 빼고 아래
for i in range(N):
    for j in range(0, i):
        arr[i][j] = 1

# 대각선 포함 위
for i in range(N):
    for j in range(i, N):
        arr[i][j] = 1

# 대각선 빼고 위
for i in range(N):
    for j in range(i+1, N):
        arr[i][j] = 1



for row in arr:
    print(*row)