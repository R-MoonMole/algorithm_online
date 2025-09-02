N = 7
# 0으로 채워진 NxN 배열생성
arr = [[0]*N for _ in range(N)]


# 기준점 r, c
r, c = 2, 3
arr[r][c] = '*'

# arr[r + 0][c + 1] = 1    # 오른쪽
# arr[r + 1][c + 0] = 2    # 아래
# arr[r + 0][c + -1] = 3    # 왼쪽
# arr[r + -1][c + 0] = 4    # 위

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]


for row in arr:
    print(*row)