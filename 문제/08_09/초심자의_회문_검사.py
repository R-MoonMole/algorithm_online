T = int(input())

for case_number in range(1, 1+T):
    string = input()
    count = 0
    pal = 1

    for length in string:
        count += 1

    for i in range(count // 2):
        if string[i] != string[-1 - i]:
            pal = 0
            break

    print(f'#{case_number} {pal}')

