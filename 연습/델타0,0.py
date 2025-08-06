N = 7
# 0으로 채워진 NxN 배열생성
arr = [[0]*N for _ in range(N)]


# 모든 r, c

# arr[r + 0][c + 1] = 1    # 오른쪽
# arr[r + 1][c + 0] = 2    # 아래
# arr[r + 0][c + -1] = 3    # 왼쪽
# arr[r + -1][c + 0] = 4    # 위

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for r in range(N):
    for c in range(N):
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 좌표를 생성하면 반드시 유효한 값인지 검사
            if 0 <= nr < N and 0 <= nc < N: # 범위를 제한하면 돌릴때 out of range가 안나오게 된다.
                arr[nr][nc] = i + 1



for row in arr:
    print(*row)