N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * N
result = []

def backtracking(x, s):
    if x == M:
        print(*result)
        return

    used = set()
    for i in range(s, N):
        if visited[i] == 0:
            if arr[i] in used:
                continue

            used.add(arr[i])
            result.append(arr[i])
            visited[i] = 1
            backtracking(x+1, i)
            result.pop()
            visited[i] = 0

backtracking(0, 0)