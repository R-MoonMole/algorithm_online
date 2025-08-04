'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

'''
#
T = int(input())
case_count = 1
result = 0

for _ in range(T):

    num, M = map(int, input().split())
    test_list_number = list(map(int, input().split()))

    max_sum = 1
    min_sum = 10000000

    for i in range(0, num - M + 1):
        number_sum = 0
        for j in range(M):
            number_sum += test_list_number[i+j]

        if number_sum < min_sum:
            min_sum = number_sum
        if number_sum > max_sum:
            max_sum = number_sum

    result = max_sum - min_sum

    print(f'#{case_count} {result}')
    case_count += 1