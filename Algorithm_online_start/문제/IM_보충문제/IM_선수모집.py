T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    max_count = -1
    number = 0


    for i in range(N):
        count = 0
        for j in range(N):
            if 0 <= i-j <= N:
                if 0 <= abs(arr[i] - arr[i-j]) <= M:
                    count += 1
        if count > max_count:
            max_count = count

    print(f'#{tc} {max_count}')