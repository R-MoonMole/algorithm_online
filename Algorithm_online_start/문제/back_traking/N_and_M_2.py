N, M = map(int, input().split())

result = []

def backtraking(x, c):
    if x == M:
        print(*result)
        return

    for i in range(c, N+1):
        result.append(i)
        backtraking(x+1, i+1)
        result.pop()

backtraking(0,1)
