'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

'''

T = int(input())
count_case = 1

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    min_num = 1000000

    for i in arr:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    result = max_num - min_num

    print(f'#{count_case} {result}')
    count_case += 1