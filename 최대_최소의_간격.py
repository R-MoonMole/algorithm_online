'''
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10

'''

T = int(input())
count_case_number = 1

for _ in range(T):
    N = int(input())
    arr = list(map(int, input(). split()))

    low_number = 10
    low_location = 0
    high_number = 0
    high_location = 0
    for i in range(0, N):
        if arr[i] < low_number:
            low_number = arr[i]
            low_location = i

        if arr[i] >= high_number:
            high_number = arr[i]
            high_location = i

    result = abs(high_location - low_location)

    print(f'#{count_case_number} {result}')
    count_case_number += 1
