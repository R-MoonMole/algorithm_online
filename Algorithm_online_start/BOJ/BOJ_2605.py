import sys
sys.stdin = open ('2605.txt', 'r')

lst = []
N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N+1):
    lst.insert(i-arr[i-1]-1, i)

print(*lst)