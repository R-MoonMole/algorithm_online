N = 5
M = 3
# 0으로 채워진 NxM 배열 생성
arr = [[0] * N for _ in range(N)]

# 모든 MxM 사각영역의 좌상단 좌표를 생성
for r1 in range(0, N-M + 1):
    for c1 in range(0, N-M + 1):
        # 좌상단(r1, c1), 너비/높이 = M
        for r in range(r1, r1+M):
            for c in range(c1, c1+M):
                arr[r][c] = 1

        # for row in arr:
        #     print(*row)
        # print('-'*10)
        #
        # for r in range(r1, r1+M):
        #     for c in range(c1, c1+M):
        #         arr[r][c] = 0
    # 이건 확인용(잘 순회하는지)



for row in arr:
    print(*row)