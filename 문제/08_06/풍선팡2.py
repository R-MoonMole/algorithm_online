'''
3
3 5
2 1 1 2 2
2 2 1 2 2
2 2 1 1 2
5 5
3 4 1 2 3
3 4 1 3 2
2 3 2 4 1
1 4 4 1 3
2 2 3 4 4
5 8
1 3 4 4 4 4 3 3
4 1 2 4 3 1 4 4
4 1 4 4 1 4 2 1
3 2 4 2 1 1 2 1
4 4 1 4 4 2 2 2

'''


T = int(input())
count_case_number = 1

for _ in range(T):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = 1

    for r in range(N):
        for c in range(M):
            pass





    # print(f'#{count_case_number} {result}')
    # count_case_number += 1