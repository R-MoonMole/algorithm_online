import sys
sys.stdin = open('11892.txt', 'r')

from collections import deque

T = int(input())

for tc in range(1, 1+T):

    N = int(input())
    lst = list(map(int, input().split()))
    count = 0

    def merge_sort(lst):
        global count
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])

        if left[-1] > right[-1]:
            count += 1
        left = deque(left)
        right = deque(right)
        arr = []

        while left and right:
            if left[0] < right[0]:
                arr.append(left.popleft())
            else:
                arr.append(right.popleft())

        arr.extend(left)
        arr.extend(right)
        return arr

    result_lst = merge_sort(lst)
    print(f'#{tc} {result_lst[N//2]} {count}')