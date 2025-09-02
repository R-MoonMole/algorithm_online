N, M = map(int, input().split())

visited = [0] * (N+1)
result = []

def backtrack(d):
    if d == M:
        print(*result)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            result.append(i)

            backtrack(d+1)

            result.pop()
            visited[i] = 0

backtrack(0)