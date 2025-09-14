import sys
sys.stdin = open('2819(2).txt', 'r')


def recur(y, x, number):
    if len(number) == 7:
        result.add(number)
        return

    if len(number) > 7:
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        recur(ny, nx, number + arr[ny][nx])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for tc in range(1, 1+T):
    arr = [input().split() for _ in range(4)]
    result = set()

    for start_y in range(4):
        for start_x in range(4):
           recur(start_y, start_x, arr[start_y][start_x])

    print(f'#{tc} {len(result)}')