# BOJ_10870 : 피보나치 수 5
# https://www.acmicpc.net/problem/10870

N = int(input())

def fibonacci(X):
    if X == 0:
        return 0

    elif X == 1:
        return 1

    else:
        return fibonacci(X-1) + fibonacci(X-2)

print(fibonacci(N))