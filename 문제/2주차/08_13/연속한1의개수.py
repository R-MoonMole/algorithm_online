T = int(input())

for count_case in range(1, T+1):
    N = int(input())
    arr = input()
    count = 0
    max_count = 0

    for i in arr:
        if i == '1':
            count += 1
            if max_count < count:
                max_count = count
        elif i == '0':
            count = 0

    print(f'#{count_case} {max_count}')
