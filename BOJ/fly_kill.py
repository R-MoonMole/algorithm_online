T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for y in range(N-M+1):
        for x in range(N-M+1):

            fly = 0
            for k in range(M):
                for l in range(M):
                    fly += arr[y+k][x+l]

            if result < fly:
                result = fly

    print(f'#{tc} {result}')