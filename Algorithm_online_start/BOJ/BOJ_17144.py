import sys
sys.stdin = open('17144.txt', 'r')

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

air_filter = []     # 공기청정기의 위치를 찾기 위함
for i in range(R):
    if arr[i][0] == -1:   # 공청기가 있으면
        air_filter.append(i)    # 추가
top, bottom = air_filter[0], air_filter[1]  # 공청기의 윗부분, 아랫부분

def diffuse():
    temp = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                amt = arr[r][c] // 5
                if amt == 0:
                    continue
                cnt = 0
                for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        temp[nr][nc] += amt
                        cnt += 1
                arr[r][c] -= amt * cnt
    # 합치기(청정기는 유지)
    for r in range(R):
        for c in range(C):
            if arr[r][c] != -1:
                arr[r][c] += temp[r][c]

# 2) 순환(공기청정기 작동)
def circulate():
    # 위쪽(반시계)
    for r in range(top-1, 0, -1):          # 왼열 위로
        arr[r][0] = arr[r-1][0]
    for c in range(0, C-1):                # 윗행 왼->오
        arr[0][c] = arr[0][c+1]
    for r in range(0, top):                # 오른열 아래로
        arr[r][C-1] = arr[r+1][C-1]
    for c in range(C-1, 1, -1):            # top행 오->왼
        arr[top][c] = arr[top][c-1]
    arr[top][1] = 0

    # 아래쪽(시계)
    for r in range(bottom+1, R-1):         # 왼열 아래로
        arr[r][0] = arr[r+1][0]
    for c in range(0, C-1):                # 아랫행 왼->오
        arr[R-1][c] = arr[R-1][c+1]
    for r in range(R-1, bottom, -1):       # 오른열 위로
        arr[r][C-1] = arr[r-1][C-1]
    for c in range(C-1, 1, -1):            # bottom행 오->왼
        arr[bottom][c] = arr[bottom][c-1]
    arr[bottom][1] = 0

    # 청정기 유지
    arr[top][0] = -1
    arr[bottom][0] = -1

for _ in range(T):
    diffuse()
    circulate()

ans = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] > 0:
            ans += arr[r][c]
print(ans)






