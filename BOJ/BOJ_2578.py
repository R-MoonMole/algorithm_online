# BOJ_2578 : 빙고
# https://www.acmicpc.net/problem/2578
import sys; sys.stdin = open('sample_input.txt')

dr = [1, 1, 0, -1, -1, -1, 0, 1] # 오른쪽부터 시계방향
dc = [0, 1, 1, 1, 0, -1, -1, -1]

my_arr = [list(map(int, input().split())) for _ in range(5)]
arr = []
for _ in range(5):
    arr.extend(list(map(int,input().split())))

count = 1
result = 0
bingo = 0

for i in range(5):
    for j in range(5):
        for k in range(25):
            if arr[k] == my_arr[i][j]:
                my_arr[i][j] = 0

                for a in range(5):
                    count = 0
                    for b in range(5):
                        if my_arr[a][b] == 0:
                            count += 1
                            if count == 5:
                                bingo += 1

                for a in range(5):
                    count = 0
                    for b in range(5):
                        if my_arr[b][a] == 0:
                            count += 1
                            if count == 5:
                                bingo += 1

                for a in range(5):
                    count = 0
                    for b in range(5):
                        if my_arr[a][a] == 0:
                            count += 1
                            if count == 5:
                                bingo += 1







print(my_arr)
print(arr)

