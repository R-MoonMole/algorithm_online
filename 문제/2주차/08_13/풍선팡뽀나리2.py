T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for count_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                for l in range(1, N-1):
                    nr =