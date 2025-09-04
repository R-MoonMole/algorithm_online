import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    count = 0
    min_count = 10**18

    def searcher(r, c):
        global count, min_count

        if r >= N or c >= N:
            return

        count += arr[r][c]

        if count > min_count:
            count -= arr[r][c]
            return

        if r == N-1 and c == N-1:
            if min_count > count:
                min_count = count
            count -= arr[r][c]
            return

        searcher(r, c + 1)
        searcher(r + 1, c)
        count -= arr[r][c]

    searcher(0, 0)

    print(f'#{tc} {min_count}')