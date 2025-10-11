import sys
sys.stdin = open('2564.txt', 'r')

W, H = map(int, input().split())
N = int(input())
result = 0
total = (W+H)*2

def posi(x, y):
    if x == 1:
        return y
    elif x == 4:
        return W + y
    elif x == 2:
        return W + H + (W - y)
    else:
        return W + H + W + (H - y)

lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append(posi(x, y))

a, b = map(int, input().split())
guard = posi(a, b)

for i in lst:
    number = abs(i-guard)
    result += min(number, total-number)

print(result)
