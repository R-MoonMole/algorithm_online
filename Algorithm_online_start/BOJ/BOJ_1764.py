import sys
sys.stdin = open('1764.txt', 'r')

N, M = map(int, input().split())
arr = set()

for _ in range(N):
    arr.add(input())

arr_check = []
for _ in range(M):
    arr_check.append(input())


print(arr)
# N, M = map(int, input().split())
# arr_dutbo = {}
#
# for _ in range(N+M):
#     word = input()
#     arr_dutbo[word] = arr_dutbo.get(word, 0) + 1
#
# target_value = 2
#
# keys = [k for k, v in arr_dutbo.items() if v == target_value]
# keys.sort()
#
# print(len(keys))
#
# for i in keys:
#     print(i)