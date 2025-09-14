import sys
sys.stdin = open('11893.txt', 'r')

T = int(input())

def binary_search_while(target):
    left = 0
    right = len(N_arr) - 1
    prev = 0

    while left <= right:
        mid = (left + right) // 2

        if N_arr[mid] == target:
            return True

        if target < N_arr[mid]:
            if prev == 1:
                return False
            right = mid - 1
            prev = 1

        else:
            if prev == 2:
                return False
            left = mid + 1
            prev = 2

    return False

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    N_arr = sorted(map(int, input().split()))
    M_arr = list(map(int, input().split()))
    result = 0

    for i in M_arr:
        if binary_search_while(i):
            result += 1

    print(f'#{tc} {result}')