import sys
sys.stdin = open('11892.txt', 'r')

T = int(input())

for tc in range(1, 1+T):

    N = int(input())
    lst = list(map(int, input().split()))

    def quicksort(arr, start, end):
        if start >= end:
            return arr

        pivot = start
        left = start + 1
        right = end

        while left <= right:
            while left <= end and arr[left] <= arr[pivot]:
                left += 1

            while right > start and arr[right] >= arr[pivot]:
                right -= 1

            if left > right:
                arr[right], arr[pivot] = arr[pivot], arr[right]

            else:
                arr[left], arr[right] = arr[right], arr[left]

        quicksort(arr, start, right - 1)
        quicksort(arr, right + 1, end)

    quicksort(lst, 0, N-1)

    print(f'#{tc} {lst[N//2]}')