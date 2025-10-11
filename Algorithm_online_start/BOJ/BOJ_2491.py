import sys
sys.stdin = open('2491.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
answer = 1
result = 1

for i in range(N-1):
    if arr[i] <= arr[i+1]:
        result += 1
        if answer < result:
            answer = result
    elif arr[i] > arr[i+1]:
        result = 1

result = 1
for j in range(N-1):
    if arr[j] >= arr[j+1]:
        result += 1
        if answer < result:
            answer = result
    elif arr[j] < arr[j+1]:
        result = 1

print(answer)