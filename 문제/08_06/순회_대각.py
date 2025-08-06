'''
3
3 4 3
2 4 5
2 3 4

'''

T = int(input())
count_case_number = 1

for _ in range(T):

    emt = 10
    arr = [[0] * emt for _ in range(emt)]
    r, c, N = map(int, input().split())

    for i in range(N):
        arr[r + i][c + i] = 1

    for j in range(N):
        arr[r + j][c + N - 1 - j] = 1

    print(f'#{count_case_number}')
    count_case_number += 1
    for row in arr:
        print(*row)