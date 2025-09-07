N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

def backtracking(x):
    if x == M:
        print(*result)
        return

    for i in range(N):
        result.append(arr[i])
        backtracking(x+1)
        result.pop()

backtracking(0)