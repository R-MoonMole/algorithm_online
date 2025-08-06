N = 7
# 0으로 채워진 NxN 배열생성
arr = [[0]*N for _ in range(N)]

# 2행1열부터 3X5행렬만 만들고 싶다.

#    1.                  2.
#    0 0 0 0 0 0 0       0 0 0 0 0 0 0
#    0 0 0 0 0 0 0       0 0 0 0 0 0 0
#    0 1 1 1 1 1 0       0 * * * * * 0
#    0 1 1 1 1 1 0       0 * * * * * 0
#    0 1 1 1 1 1 0       0 * * * * * 0
#    0 0 0 0 0 0 0       0 0 0 0 0 0 0
#    0 0 0 0 0 0 0       0 0 0 0 0 0 0

# 1. 좌상단, 우하단 좌표를 안다.
r1, c1 = 2, 1
r2, c2 = 4, 5
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        arr[r][c] = 1

# 2. 좌상단, 높이 h , 너비 w 를 안다.
r1, c1 = 2, 1
h, w = 3, 5
for r in range(r1, r1+h):
    for c in range(c1, c1+w):
        arr[r][c] = '*'







for row in arr:
    print(*row)