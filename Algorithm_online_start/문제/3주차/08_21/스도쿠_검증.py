import sys; sys.stdin = open('input_1974.txt')

T = int(input())
for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1


    while True:
        for i in range(9):
            count = 0
            for j in range(9):
                count += arr[i][j]
            if count != 45:
                result = 0
                break
        for k in range(9):
            count = 0
            for l in range(9):
                count += arr[l][k]
            if count != 45:
                result = 0
                break
        for n in range(0, 9, 3):
            for m in range(0, 9, 3):
                count = 0
                for o in range(n, n+3):
                    for p in range(m, m+3):
                        count += arr[o][p]
                if count != 45:
                    result = 0
                    break

        break
    print(f'#{tc} {result}')