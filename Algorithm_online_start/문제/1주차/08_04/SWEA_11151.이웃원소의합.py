'''
3
5
9 -1 -8 4 -1
5
4 -10 -4 9 7
10
-20 2 -19 -4 -18 19 -19 -20 -12 11

'''

count_case_number = 1
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_number = 0

    for i in range(0, N-1):

        number_sum = 0

        for j in range(2):
            number_sum += arr[i+j]

        if max_number < number_sum:
            max_number = number_sum

    print(f'#{count_case_number} {max_number}')
    count_case_number += 1