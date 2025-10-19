import sys
sys.stdin = open('1018.txt', 'r')

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

result = 64

for i in range(N - 7):
    for j in range(M - 7):

        count = 0

        for a in range(8):
            for b in range(8):
                if (a + b) % 2 == 0:
                    board = 'W'
                else:
                    board = 'B'
                if arr[i + a][j + b] != board:
                    count += 1
        rev_count = 64 - count
        result = min(rev_count, count, result)

print(result)
