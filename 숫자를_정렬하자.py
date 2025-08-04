'''
10
5
1 4 7 8 0
10
15 20 8 28 16 27 17 27 10 12
15
17 22 20 21 29 6 10 25 20 4 9 21 14 26 23
20
26 25 20 1 2 16 9 24 19 11 12 28 7 20 20 12 9 2 16 13

'''

T = int(input())
test_case_count = 1

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    result = arr

    print(f'#{test_case_count}',end=' ')
    print(*arr)
    test_case_count += 1