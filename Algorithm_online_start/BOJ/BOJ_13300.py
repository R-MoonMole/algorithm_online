import sys
sys.stdin = open('13300.txt', 'r')

N, K = map(int, input().split())
man_lst = [0] * 6
woman_lst = [0] * 6
result = 0

for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        woman_lst[y-1] += 1
    elif x == 1:
        man_lst[y-1] += 1

while man_lst and woman_lst:
    a = man_lst.pop()
    while a > 0:
        a = a - K
        result += 1
    b = woman_lst.pop()
    while b > 0:
        b = b - K
        result += 1

print(result)

N, K = map(int, input().split())
man_lst = [0] * 6
woman_lst = [0] * 6
result = 0

for _ in range(N):
    x, y = map(int, input().split())
    if x == 0:
        woman_lst[y-1] += 1
    elif x == 1:
        man_lst[y-1] += 1

while man_lst and woman_lst:
    a = man_lst.pop()
    while a > 0:
        a = a - 2
        result += 1
    b = woman_lst.pop()
    while b > 0:
        b = b - 2
        result += 1

print(result)