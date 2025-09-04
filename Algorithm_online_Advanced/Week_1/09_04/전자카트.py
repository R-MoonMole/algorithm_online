import sys
sys.stdin = open('sample_case.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    visited = [0] * (N+1)
    result = []
    min_count = 10**10

    def recur(cnt):
        global result
        if cnt == N-1:
            result += [[1] + path[:] + [1]]
            return

        for i in range(2, N+1):
            if visited[i]:
                continue

            visited[i] = 1
            path.append(i)
            recur(cnt + 1)
            path.pop()
            visited[i] = 0

    recur(0)

    for i in result:
        count = 0
        for j in range(N):
            count += arr[i[j]-1][i[j+1]-1]
        if count < min_count:
            min_count = count

    print(f'#{tc} {min_count}')