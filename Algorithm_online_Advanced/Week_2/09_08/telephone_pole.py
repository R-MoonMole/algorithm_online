import sys
sys.stdin = open('10580.txt', 'r')


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = []
    count = 0

    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])
    arr.sort(key=lambda x: x[0])

    def tele_pole(k):
        global count
        for i in range(k):
            for j in range(i+1, k):
                if arr[i][1] > arr[j][1]:
                    count += 1

    tele_pole(len(arr))
    print(f'#{tc} {count}')