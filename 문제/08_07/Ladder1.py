T = 10
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for _ in range(1, 1+T):
    count_case_number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    r_2 = 0
    c_2 = 99


    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                r_2 = j


