import sys
sys.stdin = open('2635.txt', 'r')

N = int(input())
number = 0
result = 0
lst = []
result_lst = []

while number < N:
    check = 1
    lst = [N, N - number]
    while True:
        if lst[check-1] - lst[check] >= 0:
            lst.append(lst[check-1] - lst[check])
            check += 1
        else:
            if result < len(lst):
                result = len(lst)
                result_lst = lst
            number += 1
            check = 1
            break

print(len(result_lst))
print(*result_lst)