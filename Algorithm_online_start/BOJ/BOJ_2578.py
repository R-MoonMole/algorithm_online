# BOJ_2578 : 빙고
# https://www.acmicpc.net/problem/2578
import sys; sys.stdin = open('sample_input.txt')

my_arr = [list(map(int, input().split())) for _ in range(5)]
arr = []
for _ in range(5):
    arr.extend(list(map(int, input().split())))

count = 1
result = 0
bingo = 0
speak = 0

for i in range(25):
    bingo = 0
    if result != 0:
        break

    for j in range(5):
        for k in range(5):
            if arr[i] == my_arr[j][k]:
                my_arr[j][k] = 0
                speak += 1

                for a in range(5):
                    count = 0
                    for b in range(5):
                        if my_arr[a][b] == 0:
                            count += 1
                    if count == 5:
                        bingo += 1
                    if bingo == 3:
                        result = speak

                for a in range(5):
                    count = 0
                    for b in range(5):
                        if my_arr[b][a] == 0:
                            count += 1
                    if count == 5:
                        bingo += 1
                    if bingo == 3:
                        result = speak

                count = 0
                for a in range(5):
                    if my_arr[a][a] == 0:
                        count += 1
                if count == 5:
                    bingo += 1
                if bingo == 3:
                    result = speak

                count = 0
                for a in range(5):
                    if my_arr[a][4 - a] == 0:
                        count += 1
                if count == 5:
                    bingo += 1
                if bingo == 3:
                    result = speak

print(result)


