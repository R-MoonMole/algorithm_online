import sys
sys.stdin = open('2559.txt', 'r')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = sum(arr[:K])
next_result = result

for i in range(K, N):
    next_result += arr[i]-arr[i-K]
    result = max(result, next_result)

print(result)