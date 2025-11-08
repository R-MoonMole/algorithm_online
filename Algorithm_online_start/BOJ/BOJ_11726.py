import sys
sys.stdin = open('11726.txt', 'r')

N = int(input())

if N == 1:
    print(1)

else:

    arr = [0] * (N+1)

    arr[1] = 1
    arr[2] = 2

    for i in range(3, N+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 10007

    print(arr[N])