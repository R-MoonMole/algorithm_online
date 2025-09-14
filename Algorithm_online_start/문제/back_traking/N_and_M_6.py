N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

def backtracking(x, s):
    if x == M:
        print(*result)
        return

    for i in range(s, N):
        result.append(arr[i])
        backtracking(x+1, i+1)
        result.pop()

backtracking(0, 0)
