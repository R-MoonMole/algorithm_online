import sys
sys.stdin = open('2304.txt', 'r')

N = int(input())
lst = []
max_hight = 0
first_max = 0
last_max = 0
result = 0
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort(key=lambda x:x[0])

for i in range(N):
    if lst[i][1] > max_hight:
        max_hight = lst[i][1]
        first_max = i
    if lst[i][1] >= max_hight:
        last_max = i

piv_x = lst[0][0]
piv_h = lst[0][1]
for j in range(1, first_max+1):
    if piv_h <= lst[j][1]:
        result += (lst[j][0]-piv_x) * piv_h
        piv_x = lst[j][0]
        piv_h = lst[j][1]

piv_x = lst[N-1][0]
piv_h = lst[N-1][1]
for k in range(N-2, last_max-1, -1):
    if piv_h <= lst[k][1]:
        result += (piv_x-lst[k][0]) * piv_h
        piv_x = lst[k][0]
        piv_h = lst[k][1]

result += (lst[last_max][0]+1-lst[first_max][0]) * max_hight

print(result)