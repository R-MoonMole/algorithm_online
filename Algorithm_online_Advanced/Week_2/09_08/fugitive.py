import sys
sys.stdin = open("1953.txt", 'r')

T = int(input())
for tc in range(1, 1+T):
    N, M, R, C, L = map(int, input().split())
    # N : 세로, M : 가로, R : 맨홀 세로위치, C : 맨홀 가로위치, L : 경과시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    dr = [1, 0, -1, 0] # 우 하 좌 상
    dc = [0, 1, 0, -1]

    tennel = [[0, 0, 0, 0], # 0
              [1, 1, 1, 1], # 우하좌상
              [0, 1, 0, 1], # 상하
              [1, 0, 1, 0], # 좌우
              [1, 0, 0, 1], # 상우
              [1, 1, 0, 0], # 하우
              [0, 1, 1, 0], # 하좌
              [0, 0, 1, 1]] # 상좌

    if L == 1:
        result = 1
        print(result)

    else:
        pass

    def gogo(cnt):
        if cnt == L:
            print(result)
            return

        for i in range(N):
            for j in range(M):
                if arr[i][j]

    gogo(1)