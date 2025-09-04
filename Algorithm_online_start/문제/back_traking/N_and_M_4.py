N, M = map(int, input().split())

result = []

def backtracking(x, s):
    if x == M:
        print(*result)
        return

    for i in range(s, N+1):
        result.append(i)
        backtracking(x+1, i)
        result.pop()


backtracking(0, 1)