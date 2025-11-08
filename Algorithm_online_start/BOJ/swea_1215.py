import sys
sys.stdin = open('swea_1215.txt', 'r')


for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]
    result = 0

    for i in range(8):
        for j in range(8-N+1):
            lst = arr[i][j:j+N]
            if lst == lst[::-1]:
                result += 1

    for j in range(8):
        for i in range(8-N+1):
            lst = []
            for k in range(N):
                lst.append(arr[i+k][j])
            lst = ''.join(lst)
            if lst == lst[::-1]:
                result += 1
    print(f'#{tc} {result}')