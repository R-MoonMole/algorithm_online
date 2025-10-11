import sys
sys.stdin = open('13458.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in range(N):
    number = arr[i] - B
    result += 1

    if number > 0:
        result += (number // C)
        if number % C != 0:
            result += 1

print(result)