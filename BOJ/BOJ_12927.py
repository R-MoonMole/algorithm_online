# BOJ_12927 : 배수 스위치
# https://www.acmicpc.net/problem/12927

light_list = list(input())
N = 0
count = 0
for _ in light_list:
    N += 1

for i in range(1, N+1):
    if light_list[i-1] == 'Y':
        count += 1
        for j in range(i-1, N, i):
            if light_list[j] == 'Y':
                light_list[j] = 'N'
            else:
                light_list[j] = 'Y'

print(count)
