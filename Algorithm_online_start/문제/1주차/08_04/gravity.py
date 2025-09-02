'''
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

'''

T = int(input())
count_case_number = 1

for _ in range(T):

    N = int(input())
    arr = list(map(int, input().split()))
    max_number = 0
    for i in range(0, N):
        searcher = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                searcher += 1
            elif arr[i] <= arr[j]:
                continue
        if max_number < searcher:
            max_number = searcher

    print(f'#{count_case_number} {max_number}')
    count_case_number += 1



