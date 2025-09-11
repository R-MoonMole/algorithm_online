import sys
sys.stdin = open('11897.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    number = 0
    min_number = 10e8

    def backtrack(row):
        global min_number, number

        if row == N:
            if min_number > number:
                min_number = number
            return

        for col in range(N):
            if visited[col]:
                continue

            number += arr[row][col]
            if number < min_number:
                visited[col] = 1
                backtrack(row + 1)
                visited[col] = 0
            number -= arr[row][col]

    backtrack(0)
    print(f'#{tc} {min_number}')