T = int(input())

for count_case in range(1, T+1):

    arr = list(map(int, input().split()))
    average = 0
    sum_number = 0

    for i in range(10):
        sum_number += arr[i]

    average = sum_number/10
    result = round(average)

    print(f'#{count_case} {result}')