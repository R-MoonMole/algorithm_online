N, M = map(int,input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [0] * N
result = []

def backtracking(x):
    if x == M:
        print(*result)
        return

    used = set()
    for i in range(N):
        if visited[i] == 0:
            if arr[i] in used:
                continue

            used.add(arr[i])
            visited[i] = 1
            result.append(arr[i])
            backtracking(x+1)
            visited[i] = 0
            result.pop()

backtracking(0)
