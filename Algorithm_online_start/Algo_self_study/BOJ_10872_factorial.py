# BOJ_10872 : 팩토리얼
# https://www.acmicpc.net/problem/10872

N = int(input())
cnt = 1

def factorial(X):
    global cnt

    if X == 0:
        return cnt

    cnt *= X
    factorial(X-1)

factorial(N)

print(cnt)