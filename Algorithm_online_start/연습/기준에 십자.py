dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


N = 7
# 0으로 채워진 NxN 배열생성
arr = [[0]*N for _ in range(N)]
K = 2 # 얼마나 가고싶은지
r, c = 3, 2
arr[r][c] = '*'

for dir in range(4):
    for i in range(1, K + 1):

        nr = r + dr[dir]*i
        nc = c + dc[dir]*i
        if 0 <= nr < N and 0 <= nc < N:
            arr[nr][nc] = 1
        # if nr < 0 or nr >= N or nc < 0 or nc>= N:
        #   break
        # arr[nr][nc] = 1



for row in arr:
    print(*row)