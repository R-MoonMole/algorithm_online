N = 6 # N이 짝수이면 중앙이 안겹치고, N이 홀수이면 중앙이 겹치는 걸 신경써야함
# 0으로 채워진 NxN 배열생성
arr = [[0]*N for _ in range(N)]

# 오른쪽 아래 대각선만
for i in range(N):
    arr[i][i] = 1


# 왼쪽 아래 대각선만
for i in range(N):
    arr[i][N-1-i] = 2 # N이 홀수일 땐 가운데는 2로 덮어써짐(겹치는 부분)

for row in arr:
    print(*row)