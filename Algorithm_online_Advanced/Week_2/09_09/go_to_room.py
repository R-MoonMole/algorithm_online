import sys
sys.stdin = open('4408.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    visited = [0] * 201
    arr = []
    count = 0
    for _ in range(N):
        x, y = map(int, input().split())
        x = (x+1) // 2
        y = (y+1) // 2
        if x < y:
            arr.append((x, y))
        else:
            arr.append((y, x))

    for i in range(N):
        for j in range(arr[i][0], arr[i][1]+1):
            visited[j] += 1

    for k in visited:
        if k > count:
            count = k
    print(f'#{tc} {count}')