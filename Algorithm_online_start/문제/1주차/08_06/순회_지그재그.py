'''
3
3 4 3 4
5 2 1 5
2 3 4 6

'''
T = int(input())
r, c, w, h = map(int, input().split())
N = 10
arr = [list(map(int, input().split())) for _ in range(10)]

for count_case_number in range(1, T+1):
    for i in range(w*h):
        for j in range(r, r+h):
            for k in range(c, c+w):
                arr[j][k] = 1


















