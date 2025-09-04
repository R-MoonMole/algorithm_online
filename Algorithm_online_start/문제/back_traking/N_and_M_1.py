N, M = map(int, input().split())

visited = [0] * (N+1)
result = []

def backtracking(x):
    if x == M:
        print(*result)
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            result.append(i)

            backtracking(x+1)

            result.pop()
            visited[i] = 0

backtracking(0)