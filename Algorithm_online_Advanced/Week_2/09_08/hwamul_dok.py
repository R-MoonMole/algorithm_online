import sys
sys.stdin = open("11805.txt", 'r')

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = []
    count = 0
    X = 0
    for a in range(N):
        i, j = map(int, input().split())
        arr.append((i, j))

    arr.sort(key=lambda x: x[1])

    for i in range(len(arr)):
        if X <= arr[i][0] < arr[i][1]:
            X = arr[i][1]
            count += 1
    print(f'#{tc} {count}')
