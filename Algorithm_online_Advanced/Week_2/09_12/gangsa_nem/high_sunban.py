import sys
sys.stdin = open('1486.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_height = 10e9
    arr.sort()

    def recur(height, s):
        global min_height

        if height >= B:
            if height < min_height:
                min_height = height
                return
        if height > min_height:
            return

        for i in range(s, N):
            recur(height + arr[i], i+1)

    recur(0, 0)

    print(f'#{tc} {min_height-B}')