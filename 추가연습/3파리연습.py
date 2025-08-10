N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cross_dr = [0, 1, 0, -1] # 우하좌상
cross_dc = [1, 0, -1, 0]
dia_dr = [-1, 1, 1, -1] # 우상 우하 좌하 좌상
dia_dc = [1, 1, -1, -1]

def sprey_sum(r,c,dr,dc):
    for i in range(4):
        for j in range(1, K+1):
