import sys
sys.stdin = open('10157.txt', 'r')

dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]

x, y = map(int, input().split())
goal_number = int(input())

if goal_number > x * y:
    print(0)

else:
    visited = [[0] * x for _ in range(y)]
    row, col = y - 1, 0
    dir = 0
    visited[row][col] = 1

    if goal_number == 1:
        print(col + 1, y - row)
    else:
        count = 1
        while count < goal_number:
            nr = row + dy[dir]
            nc = col + dx[dir]
            if not (0 <= nr < y and 0 <= nc < x) or visited[nr][nc]:
                dir = (dir + 1) % 4
                continue

            row, col = nr, nc
            count += 1
            visited[row][col] = count
        print(col + 1, y - row)






