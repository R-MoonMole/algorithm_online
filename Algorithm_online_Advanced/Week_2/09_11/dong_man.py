
import sys
sys.stdin = open('1865.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    probability = 1
    max_probability = 0.0
    upper = 0

    def recur(row):
        global max_probability, probability, upper

        if row == N:
            if max_probability < probability * 100:
                upper = probability
                max_probability = probability * 100
            return

        for col in range(N):
            if visited[col]:
                continue

            if arr[row][col] == 0:
                continue

            probability = probability * arr[row][col] * 0.01
            if probability > upper:
                visited[col] = 1
                recur(row + 1)
                visited[col] = 0
            probability = probability / arr[row][col] / 0.01

    recur(0)

    print(f'#{tc} {max_probability:.6f}')