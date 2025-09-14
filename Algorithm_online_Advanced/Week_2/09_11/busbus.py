import sys
sys.stdin = open('11896.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    data = list(map(int, input().split()))
    N = data[0]
    arr = data[1:]
    min_cnt = 10e9

    def gobus(now, cnt):
        global min_cnt

        if now == N - 1:
            if cnt < min_cnt:
                min_cnt = cnt
            return

        if now + arr[now] >= N-1:
            if cnt < min_cnt:
                min_cnt = cnt
            return

        if cnt >= min_cnt:
            return

        for i in range(now+1, min(N-1, now+arr[now])+1):
            gobus(i, cnt+1)

    gobus(0, 0)
    print(f'#{tc} {min_cnt}')