T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0

    def recur(x, s):
        global count

        if x == K:
            count += 1
            return

        if x > K:
            return

        for i in range(s, len(arr)):

            recur(x+arr[i], i+1)

    recur(0, 0)
    print(f'#{tc} {count}')