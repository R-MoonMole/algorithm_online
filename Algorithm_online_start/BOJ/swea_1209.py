import sys
sys.stdin = open('swea_1209.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    result = 0

    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        num_sum = 0
        for j in range(100):
            num_sum += arr[i][j]
            if result < num_sum:
                result = num_sum

    for j in range(100):
        num_sum = 0
        for i in range(100):
            num_sum += arr[i][j]
            if result < num_sum:
                result = num_sum

    num_sum = 0
    for i in range(100):
        num_sum += arr[i][i]
        if result < num_sum:
            result = num_sum
    num_sum = 0
    for i in range(100):
        num_sum += arr[99-i][i]
        if result < num_sum:
            result = num_sum

    print(f'#{tc} {result}')

