N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = []

def backtracking(x):
    if x == M:
        print(*result)
        return

    used = set()
    for i in range(N):

        if arr[i] in used:
            continue
        result.append(arr[i])
        used.add(arr[i])
        backtracking(x+1)
        result.pop()

backtracking(0)