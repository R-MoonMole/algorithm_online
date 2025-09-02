'''
3
10
0011001110
10
0000100001
10
0111001111

'''

#count_one = 0 <- 얘를 어따가 넣자

T = int(input())
count_case_number = 1

for _ in range(T):
    N = int(input())
    arr = list(map(str, input(). split()))

    for i in range(0, N):
        if arr[i] == 0:
            continue

        if arr[i] == 1:
            count_one += 1

    print(f'#{count_case_number} {count_one}')
    count_case_number += 1


