# BOJ_1941 : 소문난 칠공주
# http://acmicpc.net/problem/1941

def recur():
    if cnt == 7 and Y_cnt >= 3:
        for i in range(4):




dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

arr = [list(input().strip()) for _ in range(5)]
Y_cnt = 0
S_cnt = 0
cnt = 0

for y in range(5):
    for x in range(5):
        recur()