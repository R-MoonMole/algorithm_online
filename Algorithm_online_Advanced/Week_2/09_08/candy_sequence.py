import sys
sys.stdin = open('20551.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    A, B, C = map(int, input().split())
    result = 0

    def candy(x, y, z):
        global result
        if y >= z:
            result += abs(z-y-1)
            y = y-abs(z-y-1)

        if x >= y:
            result += abs(y-x-1)
            x = x-abs(y-x-1)

        print(f'#{tc} {result}')

    if C < 3 or B < 2:
        result = -1
        print(f'#{tc} {result}')

    elif A < B < C:
        result = 0
        print(f'#{tc} {result}')

    else:
        candy(A, B, C)