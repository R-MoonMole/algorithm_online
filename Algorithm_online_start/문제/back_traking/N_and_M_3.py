N, M = map(int, input().split())

result = []

def backtracking(x):
    if x == M:
        print(*result)
        return

    for i in range(1, N+1):

        result.append(i)
        backtracking(x+1)
        result.pop()

backtracking(0)